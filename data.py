from tkinter import *

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

def learning(list_of_y: list, file_name="a.csv"):
    list_of_lists = []
    for element in list_of_y:
        list_of_lists.append(y_dict[element])
    print(list_of_lists)

def upload_images(new_list, image_listbox):
    for filename in new_list:
        image_listbox.insert(END, filename)
