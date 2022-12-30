from hashlib import sha256

def pw2hash(InputPw):
    password = str(InputPw)
    password_input = password.encode()
    m= sha256(password_input)
    return m.hexdigest()