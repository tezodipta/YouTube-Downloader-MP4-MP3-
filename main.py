import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    format_choice = format_var.get()
    
    try:
        yt = YouTube(url)
        if format_choice == "MP4":
            stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            download_path = filedialog.askdirectory()
            stream.download(download_path)
            messagebox.showinfo("Download Complete", "Video downloaded successfully!")
        elif format_choice == "MP3":
            stream = yt.streams.filter(only_audio=True).first()
            download_path = filedialog.askdirectory()
            stream.download(download_path)
            messagebox.showinfo("Download Complete", "Audio downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

format_label = tk.Label(root, text="Select Format:")
format_label.pack()

format_var = tk.StringVar()
format_var.set("MP4")

format_radio_mp4 = tk.Radiobutton(root, text="MP4", variable=format_var, value="MP4")
format_radio_mp4.pack()

format_radio_mp3 = tk.Radiobutton(root, text="MP3", variable=format_var, value="MP3")
format_radio_mp3.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

root.mainloop()


