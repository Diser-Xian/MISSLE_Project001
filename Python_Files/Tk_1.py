import tkinter as tk

app = tk.Tk()
app.title("Counter App")
app.geometry("520x420")
app.maxsize(520, 420)
app.configure(background="white")

# Images
img = tk.PhotoImage(file=r"Photos/Strdew.png")
icon = tk.PhotoImage(file=r"/Photos/Strdew.png")
app.iconphoto(True, icon)

# Labels
greet_label = tk.Label(
    app,
    text="Welcome",
    font=("Arial", 30, "underline"),
    fg="black",
    bg=None,
    relief=tk.RAISED,
    bd=10
)
greet_label.grid(row=0, column=1)  # center at top

counter_label = tk.Label(
    app,
    text="Counter:",
    font=("Arial", 20, "bold"),
    fg="black",
    bg=None,
    relief=tk.RAISED,
    bd=10
)
counter_label.grid(row=1, column=0, padx=5, pady=5)

number = 0
value = tk.Label(
    app,
    text=number,
    font=("Arial", 20, "bold"),
    fg="black",
    bg=None,
    relief=tk.RAISED,
    bd=10
)
value.grid(row=1, column=1, padx=5, pady=5) # next to "Counter:"

# Buttons
btn_dec = tk.Button(
    app,
    text="-",
    command=lambda: [exec("global number; number-=1"), value.config(text=number)],
    font=("Arial", 20, "bold"),
    width=4
)
btn_dec.grid(row=2, column=0, padx=5, pady=5)

btn_inc = tk.Button(
    app,
    text="+",
    command=lambda: [exec("global number; number+=1"), value.config(text=number)],
    font=("Arial", 20, "bold"),
    width=4
)
btn_inc.grid(row=3, column=0, padx=5, pady=5)

app.mainloop()