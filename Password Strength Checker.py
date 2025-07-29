import re
import math
import tkinter as tk
from tkinter import messagebox

# Common weak passwords
common_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]

def calculate_entropy(password):
    charset_size = 0
    if re.search(r'[a-z]', password): charset_size += 26
    if re.search(r'[A-Z]', password): charset_size += 26
    if re.search(r'[0-9]', password): charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset_size += 32

    if charset_size == 0:
        return 0
    return len(password) * math.log2(charset_size)

def password_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Good length.")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️ Try a longer password.")
    else:
        feedback.append("❌ Too short. Use at least 8 characters.")

    # Variety
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[0-9]', password): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1

    # Dictionary word check
    for word in common_passwords:
        if word in password.lower():
            score -= 2
            feedback.append("❌ Common password detected.")
            break

    # Entropy
    entropy = calculate_entropy(password)
    if entropy < 40:
        feedback.append("⚠️ Low entropy. Add more character types.")
    else:
        feedback.append("✅ Good entropy.")

    # Final strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, entropy, feedback

# GUI Logic
def check_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Required", "Please enter a password.")
        return

    strength, entropy, feedback = password_strength(password)

    result_label.config(text=f"Strength: {strength}\nEntropy: {entropy:.2f} bits")
    feedback_text.delete("1.0", tk.END)
    for item in feedback:
        feedback_text.insert(tk.END, f"{item}\n")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check Strength", command=check_password, font=("Arial", 11)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=5)

tk.Label(root, text="Feedback:", font=("Arial", 11, "bold")).pack()
feedback_text = tk.Text(root, height=6, width=45, font=("Arial", 10))
feedback_text.pack(pady=5)

root.mainloop()
