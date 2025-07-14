import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length_str = length_entry.get().strip()
    if not length_str:
        messagebox.showerror("Missing Input", "Please enter the password length.")
        return
    try:
        length = int(length_str)
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number.")
        return
    if length < 4:
        messagebox.showwarning("Too Short", "Password length should be at least 4 characters.")
        return

    character_pool = ""
    if var_upper.get():
        character_pool += string.ascii_uppercase
    if var_lower.get():
        character_pool += string.ascii_lowercase
    if var_digits.get():
        character_pool += string.digits
    if var_special.get():
        character_pool += string.punctuation
    if not character_pool:
        messagebox.showwarning("No Options Selected", "Please select at least one character type.")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_entry.config(state='normal')
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

root = tk.Tk()
root.title("SecurePass Generator")
root.geometry("420x460")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

LABEL_FONT = ("Segoe UI", 13)
BTN_FONT = ("Segoe UI", 11, "bold")
ENTRY_FONT = ("Segoe UI", 14)

tk.Label(root, text="Secure Password Generator", font=("Segoe UI", 18, "bold"), fg="#ffd700", bg="#1e1e2f").pack(pady=15)

frame_top = tk.Frame(root, bg="#1e1e2f")
frame_top.pack(pady=5)
tk.Label(frame_top, text="Enter Password Length:", font=LABEL_FONT, bg="#1e1e2f", fg="white").grid(row=0, column=0, padx=10)
length_entry = tk.Entry(frame_top, width=5, font=ENTRY_FONT, bg="#29293d", fg="white", insertbackground='white')
length_entry.grid(row=0, column=1)

frame_check = tk.LabelFrame(root, text="Character Options", bg="#1e1e2f", fg="#ffcc80", font=LABEL_FONT)
frame_check.pack(pady=15)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(frame_check, text="Uppercase Letters", variable=var_upper, bg="#1e1e2f", fg="white", selectcolor="#29293d", font=LABEL_FONT).grid(sticky="w", padx=20)
tk.Checkbutton(frame_check, text="Lowercase Letters", variable=var_lower, bg="#1e1e2f", fg="white", selectcolor="#29293d", font=LABEL_FONT).grid(sticky="w", padx=20)
tk.Checkbutton(frame_check, text="Numbers (0-9)", variable=var_digits, bg="#1e1e2f", fg="white", selectcolor="#29293d", font=LABEL_FONT).grid(sticky="w", padx=20)
tk.Checkbutton(frame_check, text="Special Characters", variable=var_special, bg="#1e1e2f", fg="white", selectcolor="#29293d", font=LABEL_FONT).grid(sticky="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, font=BTN_FONT, bg="#ff6f61", fg="white", width=20).pack(pady=10)

password_entry = tk.Entry(root, font=ENTRY_FONT, width=30, justify="center", state='readonly', bg="#29293d", fg="#4db6ac", relief="flat")
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_password, font=BTN_FONT, bg="#4db6ac", fg="#1e1e2f", width=20).pack(pady=10)

root.mainloop()
