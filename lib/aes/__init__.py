from Crypto.Cipher import AES

from lib.bytes import wrapbytes

from lib.xor import xor


def decryptaesecb(b: bytes, k: bytes) -> bytes:
    cipher = AES.new(k, AES.MODE_ECB)
    r = cipher.decrypt(b)

    return r


def encryptaesecb(b: bytes, k: bytes) -> bytes:
    cipher = AES.new(k, AES.MODE_ECB)
    r = cipher.encrypt(b)

    return r


def decryptaescbc(b: bytes, k: bytes, iv: bytes) -> bytes:
    l = []
    wb = wrapbytes(b, 16)
    tx = iv
    for i in wb:
        tc = decryptaesecb(i, k)
        rc = xor(tc, tx)
        l.append(rc)
        tx = i
    r = b"".join(l)

    return r


def encryptaescbc(b: bytes, k: bytes, iv: bytes) -> bytes:
    l = []
    wb = wrapbytes(b, 16)
    tx = iv
    for i in wb:
        tc = xor(i, tx)
        rc = encryptaesecb(tc, k)
        l.append(rc)
        tx = rc
    r = b"".join(l)

    return r


def pkcs7pad(b: bytes, n: int) -> bytes:
    r = b + (b"%c" % (n - len(b)) * (n - len(b))) if n > len(b) and n <= 255 else b

    return r
