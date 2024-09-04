import re
import random
import tkinter as tk
from tkinter import messagebox

# Sample list of common passwords (this would be much longer in a real-world application)
COMMON_PASSWORDS = ["password", "123456", "qwerty", "abc123", "letmein"]

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Password is too common, consider choosing something more unique.")

    if re.search(r"(.)\1\1", password):
        feedback.append("Avoid using the same character three times in a row.")

    if strength == 5 and not feedback:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

def on_check_password():
    password = entry_password.get()
    strength, feedback = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"{strength}\n" + "\n".join(feedback))

def on_generate_password():
    strong_password = generate_strong_password()
    entry_password.delete(0, tk.END)
    entry_password.insert(0, strong_password)
    messagebox.showinfo("Generated Password", f"Your generated password: {strong_password}")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")

label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*", width=40)
entry_password.pack(pady=5)

button_check = tk.Button(root, text="Check Strength", command=on_check_password)
button_check.pack(pady=10)

button_generate = tk.Button(root, text="Generate Strong Password", command=on_generate_password)
button_generate.pack(pady=5)

root.mainloop()
