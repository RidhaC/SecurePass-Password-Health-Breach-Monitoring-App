import hashlib
import requests

def password_score(pw):
    length = len(pw)
    score = 0
    if length >= 8: score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in "!@#$%^&*()-_=+[{]};:'\"\\|,<.>/?`~" for c in pw): score += 1
    return score  # 0–4

def check_breach(pw):
    sha1 = hashlib.sha1(pw.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    res = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    return suffix in res.text
