from tkinter import filedialog
from learning_images import upload_images, learning
from tkinter import *
def open_files(image_listbox, language, string_var):
    """Open dialog to select files, save selected files, and upload images to a listbox.

    Opens a file dialog to allow the user to select multiple image files.
    The selected files are saved to the instance variable self.files.
    The function then calls upload_images() to upload the selected images to a listbox.

        """
    if language == "Ukraine":
        files = filedialog.askopenfilenames(
                                            title="Виберіть файли",
                                            filetypes=(("Image files", "*.png *.jpg"), ("All files", "*.*"))
                                            )
        files_list = files
        upload_images(files_list, image_listbox, string_var)
    elif language == "English":
        files = filedialog.askopenfilenames(
            title="Chose Files",
            filetypes=(("Image files", "*.png *.jpg"), ("All files", "*.*"))
        )
        files_list = files
        upload_images(files_list, image_listbox, string_var)


widgets_list = []

def naming(name, load_canvas, out_dim, h_dim, alpha, num_epochs, batch_size):
    name_path = f"resource/csv/{name.get()}.csv"
    learning(out_dim.get(), h_dim.get(), alpha.get(), num_epochs.get(), batch_size.get(), name_path,
             progress_bar=load_canvas)
