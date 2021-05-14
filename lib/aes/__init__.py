from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

from lib.data import Data


def decryptaesecb(b: Data, k: Data) -> Data:
    cipher = AES.new(k.data, AES.MODE_ECB)
    r = Data(unpad(cipher.decrypt(b.data), 16))

    return r


def encryptaesecb(b: Data, k: Data) -> Data:
    cipher = AES.new(k.data, AES.MODE_ECB)
    r = Data(cipher.encrypt(pad(b.data, 16)))

    return r


def decryptaescbc(b: Data, k: Data, iv: Data) -> Data:
    l = []
    wb = b.wrap(16)
    tx = iv
    for i in wb:
        tc = decryptaesecb(i, k)
        rc = tc ^ tx
        l.append(rc.data)
        tx = i
    r = Data(b"".join(l))

    return r


def encryptaescbc(b: Data, k: Data, iv: Data) -> Data:
    l = []
    wb = b.wrap(16)
    tx = iv
    for i in wb:
        tc = i ^ tx
        rc = encryptaesecb(tc, k)
        l.append(rc.data)
        tx = rc
    r = Data(b"".join(l))

    return r


def pkcs7pad(b: Data, n: int) -> Data:
    r = b + Data(b"%c" % (n - len(b)) * (n - len(b))) if n > len(b) and n <= 255 else b

    return r
