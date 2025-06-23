# 🔐 SecurePass: Password Strength & Breach Checker

SecurePass is a lightweight cybersecurity tool that checks the strength of a password and whether it has appeared in known data breaches. Built with Flask for the backend and HTML/JS (styled with TailwindCSS) for the frontend.

---

## 🌟 Features

- ✅ Real-time password strength scoring  
- ✅ Data breach detection using HaveIBeenPwned API  
- ✅ Responsive UI with TailwindCSS  
- ✅ Animated strength meter with color feedback  
- ✅ Show/hide password toggle

---

## 📦 Project Structure

```
securepass/
├── backend/
│   ├── app.py              # Flask server
│   ├── utils.py            # Password scoring + breach check
│   ├── requirements.txt
├── frontend/
│   ├── index.html          # Main UI
│   ├── script.js           # Logic to call backend
│   ├── styles.css          # [unused if Tailwind used via CDN]
├── tests/                  # Unit tests (TBD)
├── start_securepass.bat    # One-click launcher
```

---

## 🚀 How to Run Locally

### 1. Clone and Setup

```bash
cd securepass/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### 2. Serve Frontend

```bash
cd ../frontend
python -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.


---

## 🧪 Example Passwords

| Password        | Score        | Breached? |
|----------------|--------------|-----------|
| `123`          | Very Weak    | Yes       |
| `P@ssword123`  | Very Strong  | No        |

---

## 🔧 Todo / Improvements

- Add subdomain scanner module  
- Deploy to GitHub Pages or Render  
- Unit tests for backend utils

