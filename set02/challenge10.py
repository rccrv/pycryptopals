from base64 import b64decode

from lib.aes import decrypt_aes_cbc
from lib.data import Data


def answer() -> str:
    r = ""

    with open("files/10.txt", "rb") as f:
        b = Data(b64decode(f.read().strip()))
        k = Data(b"YELLOW SUBMARINE")
        iv = Data(b"\x00" * 16)
        r = decrypt_aes_cbc(b, k, iv).data.decode("utf-8")

    return r
