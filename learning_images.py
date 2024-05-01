from data import *
import cv2
import time
from pathlib import Path
from shutil import rmtree
import csv

def learning(file_name="a.csv", progress_bar=None):
    for path in Path('resource/images').glob('*'):
        if path.is_dir():
            rmtree(path)
        else:
            path.unlink()
    i = 0
    path_dict = {}
    for element in y_dict.items():
        percent = 50
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

    binary_list = create_bin_list(path_dict, i, progress_bar)


def upload_images(new_list, image_listbox):
    """
    New list export to filename. File name insert to image listbox
    :param new_list: export to file name
    :param image_listbox: import file name
    :return: None
    """
    for filename in new_list:
        image_listbox.insert(END, filename)
