from lib.aes import pkcs7pad
from lib.data import Data


def answer() -> bytes:
    b = Data(b"YELLOW SUBMARINE")
    n = 20

    r = pkcs7pad(b, n)

    return r.data
