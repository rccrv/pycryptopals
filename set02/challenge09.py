from lib import pkcs7pad

def answer() -> bytes:
    b = b"YELLOW SUBMARINE"
    n = 20

    r = pkcs7pad(b, n)

    return r