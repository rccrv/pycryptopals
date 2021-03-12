from Crypto.Cipher import AES

# TODO: Unifiy all sets into a single package.
from ...set01.lib import wrapbytes


def pkcs7pad(b: bytes, n: int) -> bytes:
    r = b + (b"%c" % (n - len(b)) * (n - len(b))) if n > len(b) and n <= 255 else b

    return r


def encryptaesecb(b: bytes, k: bytes) -> bytes:
    cipher = AES.new(k, AES.MODE_ECB)
    r = cipher.encrypt(b)

    return r


def encryptaescbc(b: bytes, k: bytes, iv: bytes) -> bytes:
    r = b""
    wb = wrapbytes(b, 16)
    print(wb)

    return r


def decryptaescbc(b: bytes, k: bytes) -> bytes:
    r = b""

    return r
