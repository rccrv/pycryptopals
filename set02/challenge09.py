from lib.aes import pkcs7_pad
from lib.data import Data


def answer() -> bytes:
    b = Data(b"YELLOW SUBMARINE")
    n = 4

    r = pkcs7_pad(b, n)

    return r.data
