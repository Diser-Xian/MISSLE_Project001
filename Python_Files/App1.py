from tkinter import *

# init window
root = Tk()
root.title("First App")
root.geometry("750x400")

# icon
icon = PhotoImage(file="Screenshot (5).png")
root.iconphoto(True, icon)

# background image
Bg = PhotoImage(file="Strdew.png")  # use PNG, Tkinter can't read AVIF
bg_label = Label(root, image=Bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# content
T_label = Label(root,
                text="Welcome My Developer!",
                font=("Arial", 20),
                bg="#ffffff")  # optional: set background color so text is readable
T_label.pack(pady=20, padx=20)

Qs_label = Label(root, text="Hello there! How are you?", font=("Arial", 16), bg="#ffffff")
Qs_label.pack(padx=30)

# loop window
root.mainloop()