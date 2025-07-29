# 🔐 Password Strength Checker

A simple and interactive **Password Strength Checker** built with **Python** and **Tkinter GUI**, designed to evaluate the security of passwords using entropy calculations, pattern analysis, and common password detection.

## 🚀 Features

- ✅ Real-time password strength analysis
- 🔢 Entropy calculation based on character set and length
- ⚠️ Alerts for short or weak passwords
- ❌ Detection of commonly used (and unsafe) passwords
- 🧠 Intelligent feedback with actionable suggestions
- 🖥️ Easy-to-use graphical user interface (GUI)


## 📊 How It Works

The password checker analyzes the given input using the following criteria:

1. **Length**: Passwords ≥12 characters get full points.
2. **Character Variety**: Checks for uppercase, lowercase, numbers, and special characters.
3. **Common Passwords**: Compares against a list of well-known weak passwords.
4. **Entropy**: Calculates password entropy using Shannon entropy estimation.

Strength levels:
- 🔴 Weak
- 🟡 Moderate
- 🟢 Strong

---

## 🧩 Tech Stack

- **Language**: Python 3
- **GUI**: Tkinter
- **Libraries**: `re`, `math`, `tkinter`, `messagebox`

---

## ⚙️ Installation & Usage

### Requirements
- Python 3.x installed on your system

### Run the Application

1. **Clone this repository** or copy the source code into a file:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
