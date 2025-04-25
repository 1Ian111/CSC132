import tkinter as tk
import threading


class OutOfBoundsWindow:
    def __init__(self):
        self.root = None
        self.visible = False
        self._start_thread()

    def _create_window(self):
        self.root = tk.Tk()
        self.root.title("Out of Bounds")
        self.root.configure(bg='black')
        self.root.overrideredirect(True)  # Remove window borders

        width, height = 250, 100
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width - width - 50
        y = screen_height - height - 725
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        label = tk.Label(
            self.root,
            text="Out of Bounds",
            fg="red",
            bg="black",
            font=("Arial", 20, "bold")
        )
        label.pack(expand=True)

        self.root.attributes("-topmost", True)
        self.root.withdraw()  # Start hidden

        self.root.mainloop()

    def _start_thread(self):
        t = threading.Thread(target=self._create_window, daemon=True)
        t.start()

    def show(self):
        if self.root and not self.visible:
            self.root.after(0, self.root.deiconify)
            self.visible = True

    def hide(self):
        if self.root and self.visible:
            self.root.after(0, self.root.withdraw)
            self.visible = False


# Test if run directly
if __name__ == "__main__":
    import time

    oob = OutOfBoundsWindow()
    time.sleep(1)  # Give time to build window

    print("Showing for 3 seconds")
    oob.show()
    time.sleep(3)

    print("Hiding for 2 seconds")
    oob.hide()
    time.sleep(2)

    print("Showing again for 3 seconds")
    oob.show()
    time.sleep(3)

    print("Done. You can now integrate this.")
    while True:
        time.sleep(1)
