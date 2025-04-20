import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Password length must be at least 4.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number (minimum 4).")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_special = special_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Selection Error", "Select at least one character type.")
        return

    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)

    final_password = ''.join(password)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, final_password)

def copy_password():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# GUI Setup
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("420x340")
root.configure(bg="#eafaf1")  # light mint green
root.resizable(False, False)

frame = tk.Frame(root, bg="#eafaf1", padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Labels and Inputs
tk.Label(frame, text="Password Length:", bg="#eafaf1", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
length_entry = tk.Entry(frame, font=("Segoe UI", 10))
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, pady=5)

# Checkboxes
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text="Include Uppercase (A-Z)", variable=upper_var,
               bg="#eafaf1", font=("Segoe UI", 10)).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Lowercase (a-z)", variable=lower_var,
               bg="#eafaf1", font=("Segoe UI", 10)).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Digits (0-9)", variable=digit_var,
               bg="#eafaf1", font=("Segoe UI", 10)).grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(frame, text="Include Special (!@#...)", variable=special_var,
               bg="#eafaf1", font=("Segoe UI", 10)).grid(row=4, column=0, columnspan=2, sticky="w")

# Result
tk.Label(frame, text="Generated Password:", bg="#eafaf1", font=("Segoe UI", 10)).grid(row=5, column=0, sticky="w", pady=(15, 5))
result_entry = tk.Entry(frame, width=30, font=("Segoe UI", 10), bg="white", fg="#155724")
result_entry.grid(row=5, column=1, pady=(15, 5))

# Buttons
green_btn_style = {"bg": "#28a745", "fg": "white", "activebackground": "#218838", "font": ("Segoe UI", 10, "bold")}
tk.Button(frame, text="Generate", command=generate_password, **green_btn_style).grid(row=6, column=0, pady=15)
tk.Button(frame, text="Copy", command=copy_password, **green_btn_style).grid(row=6, column=1, pady=15)

root.mainloop()
