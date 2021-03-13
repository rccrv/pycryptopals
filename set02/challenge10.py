from base64 import b64decode

from lib.aes import decryptaescbc


def answer() -> str:
    r = ""

    with open("files/10.txt", "rb") as f:
        b = b64decode(f.read().strip())
        k = b"YELLOW SUBMARINE"
        iv = b"\x00" * 16
        r = decryptaescbc(b, k, iv).decode("utf-8")

    return r
