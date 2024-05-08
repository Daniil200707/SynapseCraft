from data import listbox_list, y_dict
from tkinter import simpledialog
from random import randint
from PIL import Image, ImageEnhance

def change_brightness(y_list):
    answer = simpledialog.askfloat("Яскравість", "Введіть значення яскравості зображення")

    for image_list in y_dict.items():
        for image in image_list[1]:
            letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                            't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

            one = 1

            ten = 10

            name_len = randint(one, ten)

            name = ''
            for i in range(name_len):
                len_list = len(letters_list)
                index = randint(one, len_list) - one
                letter = letters_list[index]
                name += letter

            img = Image.open(image)
            enhancer = ImageEnhance.Brightness(img)

            img_brightness = enhancer.enhance(answer)
            img_brightness.save(f"D:\\Downloads\\{name}.png")

    destroy_all(y_list)

def destroy_all(destroy_y):
    for i in range(len(listbox_list)):
        deleted_element = listbox_list.pop()
        deleted_element.destroy()

    for j in range(len(destroy_y)):
        destroy_y.pop()
