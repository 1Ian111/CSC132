from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

# Initialize main window
root = Tk()
root.title("Controller-less Controller")
root.geometry('1280x768')
root.resizable(False, False)

# Load and resize the background image
bg_path = r"C:\Users\silwa\OneDrive\Documents\Expo\wide_blob.jpeg"
bg_image = Image.open(bg_path)
bg_image = bg_image.resize((1280, 768), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Set background
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Fonts
custom_font = font.Font(family="Helvetica", size=12, weight="bold")
title_font = font.Font(family="Helvetica", size=18, weight="bold")

# Title (centered)
title = Label(root, text="Welcome to Controller-less Controller", fg="cyan", bg="black", font=title_font)
title.place(relx=0.5, y=30, anchor='n')

# Button frame (centered)
button_frame = Frame(root, bg="", bd=0)
button_frame.place(relx=0.5, y=150, anchor='n')

# Base button style
button_kwargs = {
    "font": custom_font,
    "width": 32,
    "height": 2,
    "fg": "white",
    "bg": "#222222",
    "activebackground": "#333333",
    "bd": 0,
    "relief": FLAT,
    "highlightthickness": 0
}

# Buttons
btn1 = Button(button_frame, text="🖐 Hand Gesture Control", **button_kwargs)
btn1.pack(pady=15)

btn2 = Button(button_frame, text="💃 Body Gesture Control", **button_kwargs)
btn2.pack(pady=15)

btn3 = Button(button_frame, text="🖱 Finger Mouse Pointer", **button_kwargs)
btn3.pack(pady=15)

btn4 = Button(button_frame, text="❌ Quit", command=root.quit, **button_kwargs)
btn4.pack(pady=15)

# Run GUI
root.mainloop()
