from tkinter import *
from FilesList import widgets_list, naming, open_files
from brighthess_all import destroy_all
from data import create_listbox
from ukraine_english import clear

def translate_to_ukraine(scroll_root, root, data, out_list, name_entry, load_canvas, out_dim_entry,
                         h_dim_entry, alpha_entry, num_epochs_entry, batch_size_entry):
    destroy_all(out_list)

    elements_text = StringVar(scroll_root)

    destroy_all(deleted=widgets_list)
    files_button = Button(scroll_root, command=lambda: open_files(image_listbox, data['Language'], elements_text),
                          text="Виберіть файли")
    files_button.pack()

    image_listbox = Listbox(scroll_root, width=100, bg="#505050")
    image_listbox.pack()

    elements_label = Label(scroll_root, textvariable=elements_text)
    elements_label.pack()

    clear_button = Button(scroll_root, text='Очистси', command=lambda: clear(image_listbox))
    clear_button.pack()

    lists_button = Button(scroll_root, text="Створити перелік", command=lambda: create_listbox(scroll_root,
                                                                                               out_list,
                                                                                               image_listbox))
    lists_button.pack()

    name_label = Label(root, text="Введіть ім'я файла:")
    name_label.place(x=650, y=0)

    out_dim_label = Label(root, text="Введіть вивідні нейрони:")
    out_dim_label.place(x=900, y=0)

    batch_size_label = Label(root, text="Введіть розмір партії:")
    batch_size_label.place(x=650, y=50)

    h_dim_label = Label(root, text="Введіть скриті нейрони:")
    h_dim_label.place(x=900, y=50)

    alpha_label = Label(root, text="Введіть альфу:")
    alpha_label.place(x=650, y=100)

    num_epochs_label = Label(root, text="Введіть епохи:")
    num_epochs_label.place(x=900, y=100)

    generate_button = Button(root, text="Генерувати", command=lambda: naming(name_entry, load_canvas,
                                                                             out_dim_entry,
                                                                             h_dim_entry, alpha_entry,
                                                                             num_epochs_entry,
                                                                             batch_size_entry))
    generate_button.place(x=650, y=150)

    widgets_list.append(files_button)
    widgets_list.append(lists_button)
    widgets_list.append(name_label)
    widgets_list.append(out_dim_label)
    widgets_list.append(batch_size_label)
    widgets_list.append(h_dim_label)
    widgets_list.append(alpha_label)
    widgets_list.append(num_epochs_label)
    widgets_list.append(generate_button)
    widgets_list.append(elements_label)
    widgets_list.append(image_listbox)
    widgets_list.append(clear_button)
