from base64 import b64decode

from lib.aes import decrypt_aes_ecb_block
from lib.data import Data


def answer() -> str:
    key = Data(b"YELLOW SUBMARINE")
    r = ""

    with open("files/7.txt") as f:
        bcontent = Data(b64decode(f.read().strip()))
        r = decrypt_aes_ecb_block(bcontent, key).data.decode("utf-8")

    return r
