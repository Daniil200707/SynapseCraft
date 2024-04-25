from tkinter import *

def replace_data(images_list, listbox, image_listbox):
    for element in images_list:
        listbox.insert("end", element)
        image_listbox.delete(0, END)
