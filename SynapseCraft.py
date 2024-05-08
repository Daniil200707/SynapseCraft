from tkinter import ttk
from tkinter.ttk import Progressbar
from learning_images import *
from brighthess_all import *
from naming_translate import translate, gui_translate

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
        scrollable_frame = ScrollableFrame(root)
        scrollable_frame.pack(fill="both", expand=True)
        self.out_list = []
        self.image_listbox = Listbox(scrollable_frame.scrollable_frame, width=100, bg="#505050")
        self.image_listbox.pack()
        load_canvas = Progressbar(root, orient=HORIZONTAL, mode="determinate", length=200)
        load_canvas.place(x=750, y=150)
        name_entry = Entry(root)
        name_entry.place(x=760, y=0)
        out_dim_entry = Entry(root)
        out_dim_entry.place(x=1040, y=0)
        batch_size_entry = Entry(root)
        batch_size_entry.place(x=770, y=50)
        h_dim_entry = Entry(root)
        h_dim_entry.place(x=1040, y=50)
        menu_bar = Menu(root)
        file_menu = Menu(menu_bar)
        file_menu.add_command(label="Save", command=save)
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_command(label="Brightness", command=lambda: change_brightness(self.out_list))
        menu_bar.add_command(label="Language", command=lambda: translate(root, scrollable_frame.scrollable_frame,
                                                                         self.out_list, self.image_listbox,
                                                                         batch_size_entry, h_dim_entry, out_dim_entry,
                                                                         load_canvas, name_entry))
        gui_translate(root, scrollable_frame.scrollable_frame, self.out_list, self.image_listbox, batch_size_entry,
                      h_dim_entry, out_dim_entry, load_canvas, name_entry)
        root.configure(menu=menu_bar)
        root.mainloop()

if __name__ == "__main__":
    synapse_craft = App("300x200", "SynapseCraft", "resource/icons/brain-3449630_640.ico")
