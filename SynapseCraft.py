from tkinter import *
from tkinter import filedialog

class App:
    def __init__(self, window_size, app_name, icon_path):
        root = Tk()
        root.geometry(window_size)
        root.title(app_name)
        root.iconbitmap(icon_path)
        self.files = None
        self.files_list = []

        files_button = Button(root, command=self.open_files, text="Выберите файлы")
        files_button.pack()

        self.image_listbox = Listbox(root, width=100, bg="#505050")
        self.image_listbox.pack()

        lists_button = Button(root, text="Создать список", command=lambda: create_listbox(root))
        lists_button.pack()

        root.mainloop()

    def open_files(self):
        self.files = filedialog.askopenfilenames(
                                                title="Выберите файлы",
                                                filetypes=(("Image files", "*.png *.jpg"), ("All files", "*.*"))
                                                )
        print("Выбранные файлы:", self.files)
        self.files_list = self.files
        self.upload_images(self.files_list)

    def upload_images(self, new_list):
        # self.images_list=[]
        for filename in new_list:
            self.image_listbox.insert(END, filename)
            # self.images_list.append(filename)

def create_listbox(window):
    listbox = Listbox(window, width=100, bg="#505050")
    listbox.pack()

if __name__ == "__main__":
    synapse_craft = App("300x200", "SynapseCraft", "resource/icons/brain-3449630_640.ico")
