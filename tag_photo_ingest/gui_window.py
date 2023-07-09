import customtkinter
from tkinter import filedialog

from datetime import datetime

from tag_photo_ingest.find_all_tagged_photo import copy_files, find_image_files


def gui_window():
    today_date = datetime.now().strftime("%Y%m%d")

    root_tk = customtkinter.CTk()  # tkinter.Tk()  # create the Tk window like you normally do

    window_width = 600
    window_height = 340
    screen_width = root_tk.winfo_screenwidth()
    screen_height = root_tk.winfo_screenheight()
    x = int(screen_width / 4)
    y = int(screen_height / 2 - window_height / 2)
    root_tk.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root_tk.title("ingest tagged photo")

    label = customtkinter.CTkLabel(root_tk,
                                   text=f'All protected images will be copied to "Pictures" \n directory  in {today_date} sub folder.',
                                   fg_color="transparent",
                                   text_color='green',
                                   font=('Charter', 22)
                                   )
    label.place(relx=0.1, rely=0.15)


    def choose_folder_1():
        folder_path = filedialog.askdirectory(initialdir='/Volumes/NO NAME')
        text1 = customtkinter.CTkLabel(root_tk,
                                       text=f'Source path - {folder_path}',
                                       justify='center',
                                       fg_color="transparent",
                                       text_color='green',
                                       font=('Charter', 16)
                                       )
        text1.place(relx=0.3, rely=0.6)
        tagged_files = find_image_files(folder_path)
        return tagged_files

    button1 = customtkinter.CTkButton(master=root_tk,
                                      height=40,
                                      width=300,
                                      corner_radius=10,
                                      fg_color=("black", "gray"),  # <- tuple color for light and dark theme
                                      text="Select source folder",
                                      command=choose_folder_1)
    button1.place(relx=0.5, rely=0.5, anchor='center')

    button2 = customtkinter.CTkButton(master=root_tk,
                                      height=40,
                                      width=300,
                                      corner_radius=10,
                                      fg_color=("black", "gray"),  # <- tuple color for light and dark theme
                                      text="Copy images",
                                      command=copy_files())
    button2.place(relx=0.5, rely=0.8, anchor='center')

    root_tk.mainloop()


if __name__ == '__main__':
    gui_window()
