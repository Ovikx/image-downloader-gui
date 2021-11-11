import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from image_downloader import ImageDownloader

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.base_color = '#2b2b2b'
        self.text_color = '#ffffff'

        self.geometry('350x200')
        self.configure(bg=self.base_color)
        self.title('Image Downloader')
        self.iconbitmap('downloader.ico')

        self.create_widgets()
    
    def create_widgets(self):
        query_label = ttk.Label(self, text='Search query:', background=self.base_color, foreground=self.text_color)
        query_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        query_entry = ttk.Entry(self)
        query_entry.grid(column=1, row=0, columnspan=3, sticky=tk.W, padx=5, pady=5)

        num_label = ttk.Label(self, text='Number of images:', background=self.base_color, foreground=self.text_color)
        num_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        num_spinbox = ttk.Spinbox(self, width=5)
        num_spinbox.set(25)
        num_spinbox.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        path_label = ttk.Label(self, text='Target directory:', background=self.base_color, foreground=self.text_color)
        path_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        path_entry = ttk.Entry(self)
        path_entry.grid(column=1, row=2, columnspan=3, sticky=tk.W, padx=5, pady=5)

        browse_button = ttk.Button(self, text='Browse', command=lambda:self.open_dir_browser(path_entry))
        browse_button.grid(column=4, row=2, sticky=tk.W, pady=5)

        wd_path_label = ttk.Label(self, text='WebDriver directory:', background=self.base_color, foreground=self.text_color)
        wd_path_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        wd_path_entry = ttk.Entry(self)
        wd_path_entry.grid(column=1, row=3, columnspan=3, sticky=tk.W, padx=5, pady=5)

        wd_browse_button = ttk.Button(self, text='Browse', command=lambda:self.open_file_browser(wd_path_entry))
        wd_browse_button.grid(column=4, row=3, sticky=tk.W, pady=5)

        download_button = ttk.Button(self, text='Download', command=lambda:self.start_download(
            query_entry.get(),
            int(num_spinbox.get()),
            path_entry.get(),
            wd_path_entry.get()
        ))
        download_button.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)     
    
    def open_dir_browser(self, widget):
        directory_name = filedialog.askdirectory(
            title='Choose directory to save images to'
        )
        widget.delete(0, tk.END)
        widget.insert(0, directory_name)
    
    def open_file_browser(self, widget):
        directory_name = filedialog.askopenfilename(
            title='Select your Chrome WebDriver'
        )
        widget.delete(0, tk.END)
        widget.insert(0, directory_name)
    
    def start_download(self, query, num, dir_path, wd_path):
        image_downloader = ImageDownloader(wd_path)
        image_downloader.download_images(query, num, dir_path)

if __name__ == '__main__':
    app = App()
    app.mainloop()