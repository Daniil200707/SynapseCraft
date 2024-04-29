from tkinter import *
from cv2 import *
import time

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

def learning(file_name="a.csv", progress_bar=None):
    i = 0
    for element in y_dict.items():
        percent = 100
        expected_value = percent / len(element[1])
        i += expected_value
        if progress_bar:
            progress_bar.configure(value=i)
            progress_bar.update()
            time.sleep(1)

    if progress_bar:
        progress_bar.configure(value=100)


def upload_images(new_list, image_listbox):
    for filename in new_list:
        image_listbox.insert(END, filename)
