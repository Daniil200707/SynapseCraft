from tkinter import *
import cv2
import time
from pathlib import Path
from shutil import rmtree
from PIL import Image

y_dict = {}

def create_listbox(window, y_list: list, self_image_listbox):
    new_text = f"y{len(y_list)}"
    y_list.append(new_text)
    listbox = Listbox(window, width=100, bg="#505050")
    listbox.pack()
    button = Button(window, text=new_text, command=lambda: replace_data(self_image_listbox.get(0, END),
                                                                        listbox, self_image_listbox, new_text))
    button.pack()

def replace_data(images_list, input_listbox, image_listbox, y):
    global y_dict
    for element in images_list:
        input_listbox.insert("end", element)
        image_listbox.delete(0, END)
    y_dict[y] = images_list

def image_to_binary(image_path):
    try:
        # Открываем изображение
        img = Image.open(image_path)

        # Преобразуем изображение в бинарный список
        binary_list=list(img.tobytes())

        return binary_list
    except Exception as e:
        print(f"Ошибка при преобразовании изображения в бинарный список: {e}")
        return None

def create_bin_list(list_of_paths, count1, progress_bar):
    binary_percent = 50
    million = 1000000
    bin_list = []
    for path_to_file in list_of_paths:
        image = image_to_binary(path_to_file)
        count1 += binary_percent / len(path_to_file)
        bin_sum = 0
        for bin_code in image:
            bin_sum += bin_code
        if progress_bar:
            progress_bar.configure(value=count1)
            progress_bar.update()
        print(bin_sum / million)
        bin_list.append(bin_sum / million)

    if progress_bar:
        progress_bar.configure(value=100)

    return bin_list

def learning(file_name="a.csv", progress_bar=None):
    for path in Path('resource/images').glob('*'):
        if path.is_dir():
            rmtree(path)
        else:
            path.unlink()
    i = 0
    path_list = []
    for element in y_dict.items():
        percent = 50
        expected_value = percent / len(element[1])
        i += expected_value
        for filename in element[1]:
            img = cv2.imread(filename)
            img = cv2.resize(img, (200, 100))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.Canny(img, 90, 90)
            file_path = f"resource/images/{time.time()}.png"
            cv2.imwrite(file_path, img)
            path_list.append(file_path)
        if progress_bar:
            progress_bar.configure(value=i)
            progress_bar.update()
            time.sleep(1)

    binary_list = create_bin_list(path_list, i, progress_bar)

def upload_images(new_list, image_listbox):
    for filename in new_list:
        image_listbox.insert(END, filename)
