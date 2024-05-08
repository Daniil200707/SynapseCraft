from tkinter import *
from translate import translate_to_ukraine, translate_to_english
import yaml

def gui_translate(root, scroll_root, out_list, image_listbox, batch_size_entry, h_dim_entry, out_dim_entry,
                  load_canvas, name_entry):
    with open("resource/conf.yaml", "r") as file:
        data = yaml.safe_load(file)
    num_epochs_entry = Entry(root)
    num_epochs_entry.place(x=1000, y=100)
    alpha_entry = Entry(root)
    alpha_entry.place(x=750, y=100)
    if data['Language'] == 'Ukraine':
        translate_to_ukraine(scroll_root, root, image_listbox, data, out_list, name_entry, load_canvas, out_dim_entry,
                             h_dim_entry, alpha_entry, num_epochs_entry, batch_size_entry)
    if data['Language'] == 'English':
        translate_to_english(scroll_root, root, image_listbox, data, out_list, name_entry, load_canvas, out_dim_entry,
                             h_dim_entry, alpha_entry, num_epochs_entry, batch_size_entry)

def translate(root, scroll_root, out_list, image_listbox, batch_size_entry, h_dim_entry, out_dim_entry,
              load_canvas, name_entry):
    with open("resource/conf.yaml", "r") as file:
        data = yaml.safe_load(file)

    new_data = {}

    if data['Language'] == 'Ukraine':
        new_data['Language'] = 'English'
    elif data['Language'] == 'English':
        new_data['Language'] = 'Ukraine'

    with open("resource/conf.yaml", "w") as file:
        yaml.dump(new_data, file)

        gui_translate(root, scroll_root, out_list, image_listbox, batch_size_entry, h_dim_entry, out_dim_entry,
                      load_canvas, name_entry)
