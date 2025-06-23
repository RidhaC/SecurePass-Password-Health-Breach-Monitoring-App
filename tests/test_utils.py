from backend.utils import password_score, check_breach

def test_password_score():
    assert password_score("123") == 1
    assert password_score("Strong123!") >= 3

def test_check_breach():
    assert isinstance(check_breach("password"), bool)
