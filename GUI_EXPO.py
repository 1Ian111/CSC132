from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

# Initialize main window
root = Tk()
root.title("Controller-less Controller")
root.geometry('900x600')
root.resizable(False, False)

# Load and resize the background image
bg_path = r"C:\Users\silwa\OneDrive\Desktop\CSC_Assignments\CSC132\wide_blob.jpeg"
bg_image = Image.open(bg_path)
bg_image = bg_image.resize((900, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Set background
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Fonts
custom_font = font.Font(family="Helvetica", size=11, weight="bold")
title_font = font.Font(family="Helvetica", size=16, weight="bold")

# Title
title = Label(root, text="Welcome to Controller-less Controller", fg="cyan", bg="black", font=title_font)
title.place(x=230, y=20)

# Button frame
button_frame = Frame(root, bg="", bd=0)
button_frame.place(x=325, y=120)

# Base button style (no borders, flat)
button_kwargs = {
    "font": custom_font,
    "width": 30,
    "height": 2,
    "fg": "white",
    "bg": "#222222",               # dark gray to blend with background
    "activebackground": "#333333",
    "bd": 0,
    "relief": FLAT,
    "highlightthickness": 0
}

# Buttons
btn1 = Button(button_frame, text="🖐 Hand Gesture Control", **button_kwargs)
btn1.pack(pady=12)

btn2 = Button(button_frame, text="💃 Body Gesture Control", **button_kwargs)
btn2.pack(pady=12)

btn3 = Button(button_frame, text="🖱 Finger Mouse Pointer", **button_kwargs)
btn3.pack(pady=12)

btn4 = Button(button_frame, text="❌ Quit", command=root.quit, **button_kwargs)
btn4.pack(pady=12)

# Run GUI
root.mainloop()
