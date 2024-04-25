from tkinter import *
import time

def create_listbox(window, text, self_image_listbox):
    new_text = text + str(time.time())
    listbox = Listbox(window, width=100, bg="#505050")
    listbox.pack()
    button = Button(window, text=new_text, command=lambda: replace_data(self_image_listbox.get(0, END),
                                                                        listbox, self_image_listbox))
    button.pack()

def replace_data(images_list, input_listbox, image_listbox):
    for element in images_list:
        input_listbox.insert("end", element)
        image_listbox.delete(0, END)
