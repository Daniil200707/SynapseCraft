from tkinter import *
from PIL import Image
import shutil

y_dict = {}
listbox_list = []

def create_listbox(window, y_list: list, self_image_listbox):
    """
    Writes number of outputs and create buttons and listbox
    :param window: the root of tkinter
    :param y_list: the list osf saves y of dataset
    :param self_image_listbox: the listbox in class
    :return: none
    """
    new_text = f"y{len(y_list)}"
    y_list.append(new_text)
    listbox = Listbox(window, width=100, bg="#505050")
    listbox.pack()
    button = Button(window, text=new_text, command=lambda: replace_data(self_image_listbox.get(0, END),
                                                                        listbox, self_image_listbox, new_text))
    button.pack()
    listbox_list.append(listbox)

def replace_data(images_list, input_listbox, image_listbox, y):
    """
    replace data to inner listbox
    :param images_list: the list of images
    :param input_listbox: to replace data
    :param image_listbox: to export data for input_listbox
    :param y: number for y
    :return: none
    """
    global y_dict
    for element in images_list:
        input_listbox.insert("end", element)
        image_listbox.delete(0, END)
    y_dict[y] = images_list

def image_to_binary(image_path):
    """
    convert image to binary code
    :param image_path: path to file of image
    :return: binary list or None
    """
    try:
        img = Image.open(image_path)

        binary_list = list(img.tobytes())

        return binary_list
    except Exception as e:
        print(f"Помилка при перетворенні зображення на бінарний список: {e}")
        return None

def create_bin_list(list_of_paths: dict, count1: int, progress_bar):
    """
    Crete bin_dict
    :param list_of_paths: Path to images in list
    :param count1: Count progress percent
    :param progress_bar: The tkinter widget
    :return: bin_dict
    """
    binary_percent = 25
    million = 1000000
    bin_dict = {}
    for path_to_file in list_of_paths.items():
        bin_list = []
        for element in path_to_file[1]:
            image = image_to_binary(element)
            count1 += binary_percent / len(list_of_paths)
            bin_sum = 0
            for bin_code in image:
                bin_sum += bin_code
            if progress_bar:
                progress_bar.configure(value=count1)
                progress_bar.update()
            print(bin_sum / million)
            bin_list.append(bin_sum / million)
        bin_dict[path_to_file[0]] = bin_list

    return bin_dict, count1

def save():
    shutil.move("resource/arr/b1.np", "C:\\Users\\Валюша\\Downloads")
    shutil.move("resource/arr/b2.np", "C:\\Users\\Валюша\\Downloads")
    shutil.move("resource/arr/W1.np", "C:\\Users\\Валюша\\Downloads")
    shutil.move("resource/arr/W2.np", "C:\\Users\\Валюша\\Downloads")
