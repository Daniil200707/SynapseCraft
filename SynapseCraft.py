from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Progressbar
from learning_images import *
from brighthess_all import *

class ScrollableFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        Initialization method for the ScrollableFrame class.

        Parameters:
            parent: tk.Widget
                The parent widget for this ScrollableFrame.
            *args: tuple
                Optional positional arguments.
            **kwargs: dict
                Optional keyword arguments.

        This method initializes the ScrollableFrame by creating a canvas and a scrollbar. It also creates a scrollable
        frame within the canvas to contain other widgets. The scrollable frame is bound to the "<Configure>" event of
        the canvas, so that the scroll region is updated whenever the size of the frame changes. The canvas is
        then configured to display the scrollable frame and linked to the scrollbar for vertical scrolling. Finally,
        the canvas and scrollbar are packed within the ScrollableFrame widget.

        """
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
        """
        Initialize the GUI application with specified window size, application name, and icon path.

        Args:
            window_size (str): The size of the application window in the format "width x height".
            app_name (str): The name of the application.
            icon_path (str): The path to the icon file for the application.

        Creates:
            - The main Tkinter window with the specified window size, title, and icon.
            - Initializes instance variables for file handling.
            - Creates a scrollable frame within the main window.
            - Creates a button for selecting files and a listbox to display selected files.
            - Creates a progress bar for displaying loading progress.
            - Creates input fields and labels for specifying parameters.
            - Creates a button for generating output based on specified parameters.

        Note:
            - The `create_listbox` function is assumed to be defined elsewhere and used as a callback.
            - The `learning` function is assumed to be defined elsewhere and used as a callback.
        """
        root = Tk()
        root.geometry(window_size)
        root.title(app_name)
        root.iconbitmap(icon_path)
        self.files = None
        self.files_list = []
        scrollable_frame = ScrollableFrame(root)
        scrollable_frame.pack(fill="both", expand=True)
        self.out_list = []

        files_button = Button(scrollable_frame.scrollable_frame, command=self.open_files, text="Виберіть файли")
        files_button.pack()

        self.image_listbox = Listbox(scrollable_frame.scrollable_frame, width=100, bg="#505050")
        self.image_listbox.pack()
        load_canvas = Progressbar(root, orient=HORIZONTAL, mode="determinate", length=200)
        load_canvas.place(x=750, y=150)

        lists_button = Button(scrollable_frame.scrollable_frame,
                              text="Створити перелік",
                              command=lambda: create_listbox(scrollable_frame.scrollable_frame, self.out_list,
                                                             self.image_listbox))
        lists_button.pack()

        name_label = Label(root, text="Введіть ім'я файла:")
        name_label.place(x=650, y=0)
        name_entry = Entry(root)
        name_entry.place(x=760, y=0)
        out_dim_label = Label(root, text="Введіть вивідні нейрони:")
        out_dim_label.place(x=900, y=0)
        out_dim_entry = Entry(root)
        out_dim_entry.place(x=1040, y=0)
        batch_size_label = Label(root, text="Введіть розмір партії:")
        batch_size_label.place(x=650, y=50)
        batch_size_entry = Entry(root)
        batch_size_entry.place(x=770, y=50)
        h_dim_label = Label(root, text="Введіть скриті нейрони:")
        h_dim_label.place(x=900, y=50)
        h_dim_entry = Entry(root)
        h_dim_entry.place(x=1040, y=50)
        alpha_label = Label(root, text="Введіть альфу:")
        alpha_label.place(x=650, y=100)
        alpha_entry = Entry(root)
        alpha_entry.place(x=750, y=100)
        num_epochs_label = Label(root, text="Введіть епохи:")
        num_epochs_label.place(x=900, y=100)
        num_epochs_entry = Entry(root)
        num_epochs_entry.place(x=1000, y=100)

        generate_button = Button(root, text="Генерувати", command=lambda: naming(name_entry, load_canvas, out_dim_entry,
                                                                                 h_dim_entry, alpha_entry,
                                                                                 num_epochs_entry, batch_size_entry))
        generate_button.place(x=650, y=150)

        menu_bar = Menu(root)

        file_menu = Menu(menu_bar)
        file_menu.add_command(label="Зберегти", command=save)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        menu_bar.add_command(label="Яскравість", command=lambda: change_brightness(self.out_list))

        root.configure(menu=menu_bar)

        root.mainloop()

    def open_files(self):
        """Open dialog to select files, save selected files, and upload images to a listbox.

                Opens a file dialog to allow the user to select multiple image files.
                The selected files are saved to the instance variable self.files.
                The function then calls upload_images() to upload the selected images to a listbox.

                """
        self.files = filedialog.askopenfilenames(
                                                title="Виберіть файли",
                                                filetypes=(("Image files", "*.png *.jpg"), ("All files", "*.*"))
                                                )
        self.files_list = self.files
        upload_images(self.files_list, self.image_listbox)

def naming(name, load_canvas, out_dim, h_dim, alpha, num_epochs, batch_size):
    name_path = f"resource/csv/{name.get()}.csv"
    learning(out_dim.get(), h_dim.get(), alpha.get(), num_epochs.get(), batch_size.get(), name_path,
             progress_bar=load_canvas)


if __name__ == "__main__":
    synapse_craft = App("300x200", "SynapseCraft", "resource/icons/brain-3449630_640.ico")
