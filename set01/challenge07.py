from base64 import b64decode

from lib import decryptaesecb


def answer() -> str:
    key = b"YELLOW SUBMARINE"
    r = ""

    with open("files/7.txt") as f:
        bcontent = b64decode(f.read().strip())
        r = decryptaesecb(bcontent, key).decode("utf-8")

    return r
