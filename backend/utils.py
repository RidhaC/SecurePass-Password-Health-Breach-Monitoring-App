import hashlib
import math
import requests

# Estimate entropy based on character sets used
def password_entropy(password: str) -> float:
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in "!@#$%^&*()-_=+[{]};:'\"\\|,<.>/?`~" for c in password):
        charset += 32

    if charset == 0:
        return 0.0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

# Convert entropy into score buckets
def password_score(password: str) -> int:
    ent = password_entropy(password)
    if ent < 28:
        return 0  # Very Weak
    elif ent < 35:
        return 1  # Weak
    elif ent < 59:
        return 2  # Moderate
    elif ent < 80:
        return 3  # Strong
    else:
        return 4  # Very Strong

# Use HaveIBeenPwned k-anonymity search
def check_breach(password: str) -> bool:
    try:
        sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return False
        hashes = (line.split(':')[0] for line in response.text.splitlines())
        return suffix in hashes
    except Exception:
        return False  # Fail closed for safety
