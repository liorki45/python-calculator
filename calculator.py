import tkinter as tk
from tkinter import messagebox

#Define the color palette
bg_color = "#F0F0F0"
button_bg_color = "#D1D1D1"
button_fg_color = "#333333"
button_active_bg_color = "#BBBBBB"

def on_button_click(event):
    current_text = event.widget.cget("text")
    if current_text == "=":
        try:
            expression = display.get()
            result = str(eval(expression))
            display.set(result)
        except Exception as e:
            display.set("Error")
            messagebox.showerror("Error", "Invaild Expression")
    elif current_text == "C":
        display.set("")
    else:
        display.set(display.get() + current_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")  # Set the initial size

# Configure the root window's background color
root.configure(bg=bg_color)

display = tk.StringVar()
display.set("")

entry = tk.Entry(root, textvar=display, font=("Arial", 20), bd=10,
relief="ridge", justify="right")
entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

buttons = [
    ("7", "8", "9", "/", "("),
    ("4", "5", "6", "*", ")"),
    ("1", "2", "3", "-", "="),
    ("C", "0", ".", "+")
]

for button_row in buttons:
    row_frame = tk.Frame(root, bg=bg_color)
    row_frame.pack(fill=tk.BOTH, expand=True)

    for button_text in button_row:
        button = tk.Button(row_frame, text=button_text,
font=("Arial", 16, "bold"),
                           relief="ridge", bd=3,
bg=button_bg_color, fg=button_fg_color,
activebackground=button_active_bg_color)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=
5, pady=5)
        button.bind("<Button-1>", on_button_click)

root.mainloop()
