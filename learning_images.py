from data import *
import cv2
import time
from pathlib import Path
from shutil import rmtree
import csv
import Learning as Lg

def learning(out_dim, h_dim, alpha, num_epochs, batch_size, file_name="resource/csv/new_data.csv", progress_bar=None):
    for path in Path('resource/images').glob('*'):
        if path.is_dir():
            rmtree(path)
        else:
            path.unlink()
    i = 0
    path_dict = {}
    for element in y_dict.items():
        percent = 25
        expected_value = percent / len(element[1])
        i += expected_value
        path_list = []
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
        path_dict[element[0]] = path_list

    binary_list, data_counter = create_bin_list(path_dict, i, progress_bar)

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y"])

    counter2 = write_csv(file_name, progress_bar, binary_list, data_counter)
    Lg.new_learn(int(out_dim), int(h_dim), float(alpha), int(num_epochs), int(batch_size), progress_bar, counter2,
                 file_name)


def upload_images(new_list, image_listbox):
    """
    New list export to filename. File name insert to image listbox
    :param new_list: export to file name
    :param image_listbox: import file name
    :return: None
    """
    for filename in new_list:
        image_listbox.insert(END, filename)

def write_csv(csv_name: str, csv_progress_bar, data: dict, count2: int):
    for element in data.items():
        data_percent = 25
        data_value = data_percent / len(data)
        count2 += data_value

        for float_number in element[1]:
            data_row = [float_number, element[0][1:]]
            with open(csv_name, "a", newline="") as data_file:
                csv_writer = csv.writer(data_file)
                csv_writer.writerow(data_row)

        if csv_progress_bar:
            csv_progress_bar.configure(value=count2)
            csv_progress_bar.update()

        return count2
