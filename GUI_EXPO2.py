from tkinter import *
from tkinter import font
import random

# Initialize main window
root = Tk()
root.title("Controller-less Controller")
root.geometry('900x600')
root.configure(bg='#0f0f0f')
root.resizable(False, False)

# Fonts
title_font = font.Font(family="Consolas", size=20, weight="bold")
button_font = font.Font(family="Consolas", size=12)

# Canvas for animated-style MediaPipe-ish mesh
canvas = Canvas(root, width=900, height=600, bg="#0f0f0f", highlightthickness=0)
canvas.place(x=0, y=0)

# Generate random MediaPipe-style node mesh
nodes = [(random.randint(50, 850), random.randint(50, 550)) for _ in range(30)]

# Draw connections (random pairs)
for i in range(len(nodes)):
    x1, y1 = nodes[i]
    for j in range(i + 1, len(nodes)):
        if random.random() < 0.1:  # 10% chance to connect
            x2, y2 = nodes[j]
            canvas.create_line(x1, y1, x2, y2, fill="#00ffff", width=1)

# Draw nodes (dots)
for x, y in nodes:
    canvas.create_oval(x-3, y-3, x+3, y+3, fill="#00ffff", outline="")

# Title Label
title = Label(root, text="> Welcome to Controller-less Controller <", fg="#39ff14",
              bg="#0f0f0f", font=title_font)
title.place(relx=0.5, y=60, anchor='center')

# Glowing button function
def create_glow_button(text, command=None):
    return Button(root, text=text,
                  font=button_font,
                  fg="#00ffff",
                  bg="#1a1a1a",
                  activebackground="#111111",
                  activeforeground="#00ffff",
                  relief="flat",
                  padx=20, pady=12,
                  bd=3,
                  highlightthickness=2,
                  highlightbackground="#00ffff",
                  command=command)

# Place buttons
create_glow_button("🖐 Hand Gesture Buttons").place(relx=0.5, y=180, anchor='center')
create_glow_button("🕺 Full Body Movement").place(relx=0.5, y=250, anchor='center')
create_glow_button("🖱 Mouse Hand Gesture").place(relx=0.5, y=320, anchor='center')
create_glow_button("🚪 Quit", command=root.quit).place(relx=0.5, y=390, anchor='center')

# Run it
root.mainloop()
