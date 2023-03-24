import tkinter
import customtkinter
from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress_percentage.configure(text=per + '%')
    progress_percentage.update()
    
    # Update Progress Bar
    progress_bar.set(float(percentage_of_completion / 100))

def startDownload():
    try:
        youtubeLink = link.get()
        youtubeObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        video = youtubeObject.streams.get_highest_resolution()
        title.configure(text=youtubeObject.title, text_color="white")
        finish_label.configure(text="")
        video.download()
    except:
        finish_label.configure(text="Error parsing the URL", text_color="red")
        return

    finish_label.configure(text="Downloaded", text_color="white")
    
# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack(pady=10)

# Progress Percentage
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=startDownload)
download_button.pack(padx=10, pady=10)

# Run App
app.mainloop()

