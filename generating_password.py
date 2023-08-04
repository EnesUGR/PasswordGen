import random
import string


def generate_password(length:int,uppers:bool,lowers:bool,digits:bool,special:bool) -> str:
    all_chars = []

    if uppers: all_chars.extend(string.ascii_uppercase)
    if lowers: all_chars.extend(string.ascii_lowercase)
    if digits: all_chars.extend(string.digits)
    if special: all_chars.extend(string.punctuation)

    password = random.choices(all_chars, k=length)
    password = "".join(password)

    return password

