from tkinter import *
from tkinter import filedialog

class App:
    def __init__(self, window_size, app_name, icon_path):
        root = Tk()
        root.geometry(window_size)
        root.title(app_name)
        root.iconbitmap(icon_path)
        self.files = None

        files_button = Button(root, command=self.open_files, text="")
        files_button.pack()

        root.mainloop()

    def open_files(self):
        self.files = filedialog.askopenfilenames(
                                                title="Выберите файлы",
                                                filetypes=(("Image files", "*.png"), ("All files", "*.*"))
                                                )
        print("Выбранные файлы:", self.files)

if __name__ == "__main__":
    synapse_craft = App("300x200", "SynapseCraft", "resource/icons/brain-3449630_640.ico")
