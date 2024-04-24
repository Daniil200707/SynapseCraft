from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import time

class ScrollableFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.canvas = Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

class App:
    def __init__(self, window_size, app_name, icon_path):
        root = Tk()
        root.geometry(window_size)
        root.title(app_name)
        root.iconbitmap(icon_path)
        self.files = None
        self.files_list = []
        scrollable_frame = ScrollableFrame(root)
        scrollable_frame.pack(fill="both", expand=True)

        files_button = Button(scrollable_frame.scrollable_frame, command=self.open_files, text="Выберите файлы")
        files_button.pack()

        self.image_listbox = Listbox(scrollable_frame.scrollable_frame, width=100, bg="#505050")
        self.image_listbox.pack()

        lists_button = Button(scrollable_frame.scrollable_frame,
                              text="Создать список",
                              command=lambda: self.create_listbox(scrollable_frame.scrollable_frame, "1"))
        lists_button.pack()

        name_label = Label(root, text="Input name:")
        name_label.place(x=650, y=0)

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

    def create_listbox(self, window, text):
        new_text = text + str(time.time())
        listbox = Listbox(window, width=100, bg="#505050")
        listbox.pack()
        button = Button(window, text=new_text, command=lambda: replace_data(self.image_listbox.get(0, END)))
        button.pack()

        def replace_data(images_list):
            for element in images_list:
                listbox.insert("end", element)
                self.image_listbox.delete(0, END)

if __name__ == "__main__":
    synapse_craft = App("300x200", "SynapseCraft", "resource/icons/brain-3449630_640.ico")
