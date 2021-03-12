from lib import encryptaescbc

def answer() -> str:
    r = ""

    with open("files/10.txt", "rb") as f:
        b = f.read()
        k = b"YELLOW SUBMARINE"
        iv = "\x00" * 16
        encryptaescbc(b, k, iv)

    return r
