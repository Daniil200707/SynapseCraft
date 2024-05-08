import random
import numpy as np
import datasets
import time

INPUT_DIM = 1

def relu(t):
    return np.maximum(t, 0)

def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)

def softmax_batch(t):
    out = np.exp(t)
    return out / np.sum(out, axis=1, keepdims=True)

def sparse_cross_entropy(z, y):
    return -np.log(z[0, y])

def sparse_cross_entropy_batch(z, y):
    return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

def to_full(y, num_classes):
    y_full = np.zeros((1, num_classes))
    y_full[0, y] = 1
    return y_full

def to_full_batch(y, num_classes):
    y_full = np.zeros((len(y), num_classes))
    for j, yj in enumerate(y):
        y_full[j, yj] = 1
    return y_full

def relu_deriv(t):
    return (t >= 0).astype(float)

def new_learn(out_dim, h_dim, alpha, num_epochs, batch_size, progress_bar, counter, data):
    i = counter

    learn = datasets.open_csv(data)
    learn = learn.to_numpy()
    data = learn[:, :-1]
    target = learn[:, -1]
    target = [int(t) for t in target]
    datasets1 = [(data[i][None, ...], target[i]) for i in range(len(target))]
    print(datasets1)

    W1 = np.random.rand(INPUT_DIM, h_dim)
    b1 = np.random.rand(1, h_dim)
    W2 = np.random.rand(h_dim, out_dim)
    b2 = np.random.rand(1, out_dim)

    W1 = (W1 - 0.5) * 2 * np.sqrt(1/INPUT_DIM)
    b1 = (b1 - 0.5) * 2 * np.sqrt(1/INPUT_DIM)
    W2 = (W2 - 0.5) * 2 * np.sqrt(1/h_dim)
    b2 = (b2 - 0.5) * 2 * np.sqrt(1/h_dim)

    loss_arr = []

    for ep in range(num_epochs):
        random.shuffle(datasets1)
        for i in range(len(datasets1) // batch_size):

            batch_x, batch_y = zip(*datasets1[i*batch_size : i*batch_size+batch_size])
            x = np.concatenate(batch_x, axis=0)
            y = np.array(batch_y)

            # Forward
            t1 = x @ W1 + b1
            h1 = relu(t1)
            t2 = h1 @ W2 + b2
            z = softmax_batch(t2)
            E = np.sum(sparse_cross_entropy_batch(z, y))

            # Backward
            y_full = to_full_batch(y, out_dim)
            dE_dt2 = z - y_full
            dE_dW2 = h1.T @ dE_dt2
            dE_db2 = np.sum(dE_dt2, axis=0, keepdims=True)
            dE_dh1 = dE_dt2 @ W2.T
            dE_dt1 = dE_dh1 * relu_deriv(t1)
            dE_dW1 = x.T @ dE_dt1
            dE_db1 = np.sum(dE_dt1, axis=0, keepdims=True)

            # Update
            W1 = W1 - alpha * dE_dW1
            b1 = b1 - alpha * dE_db1
            W2 = W2 - alpha * dE_dW2
            b2 = b2 - alpha * dE_db2

            loss_arr.append(E)

            i += 20 / num_epochs

            if progress_bar:
                progress_bar.configure(value=i)
                progress_bar.update()

    print(type(W1))

    file = open("resource/arr/W1.np", "wb")
    # save array to the file
    np.save(file, W1)

    file = open("resource/arr/b1.np", "wb")
    np.save(file, b1)

    file = open("resource/arr/W2.np", "wb")
    np.save(file, W2)

    file = open("resource/arr/b2.np", "wb")
    np.save(file, b2)
    # close the file

    def predict(x):
        t1 = x @ W1 + b1
        h1 = relu(t1)
        t2 = h1 @ W2 + b2
        z = softmax_batch(t2)
        return z

    def calc_accuracy():
        correct = 0
        for x, y in datasets1:
            z = predict(x)
            y_pred = np.argmax(z)
            if y_pred == y:
                correct += 1
        acc = correct / len(datasets1)
        return acc

    accuracy = calc_accuracy()
    print("Accuracy:", accuracy)

    import matplotlib.pyplot as plt
    plt.plot(loss_arr)
    plt.show()

    if progress_bar:
        progress_bar.configure(value=100)
        time.sleep(1)
        progress_bar.configure(value=0)
