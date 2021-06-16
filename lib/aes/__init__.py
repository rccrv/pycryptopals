from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

from lib.data import Data


def decrypt_aes_ecb_block(b: Data, k: Data) -> Data:
    if len(b) % 16 != 0:
        raise ValueError("Data must be aligned to 16 bytes")
    if len(k) != 16:
        raise ValueError("Key must be 16 bytes long")

    cipher = AES.new(k.data, AES.MODE_ECB)
    r = Data(cipher.decrypt(b.data))

    return r


def encrypt_aes_ecb_block(b: Data, k: Data) -> Data:
    if len(b) % 16 != 0:
        raise ValueError("Data must be aligned to 16 bytes")
    if len(k) != 16:
        raise ValueError("Key must be 16 bytes long")

    cipher = AES.new(k.data, AES.MODE_ECB)
    r = Data(cipher.encrypt(b.data))

    return r


def decrypt_aes_ecb(b: Data, k: Data) -> Data:
    if len(b) % 16 != 0:
        raise ValueError("Data must be aligned to 16 bytes")
    if len(k) != 16:
        raise ValueError("Key must be 16 bytes long")

    cipher = AES.new(k.data, AES.MODE_ECB)
    r = Data(unpad(cipher.decrypt(b.data), 16))

    return r


def encrypt_aes_ecb(b: Data, k: Data) -> Data:
    d = pkcs7_pad(b, len(b) + (16 - len(b) % 16)) if len(b) % 16 != 0 else b
    if len(k) != 16:
        raise ValueError("Key must be 16 bytes long")

    cipher = AES.new(k.data, AES.MODE_ECB)
    r = Data(cipher.encrypt(d.data))

    return r


# TODO: Test this function a little further
def decrypt_aes_cbc(b: Data, k: Data, iv: Data) -> Data:
    l = []
    wb = b.wrap(16)
    tx = iv
    for i in wb:
        tc = decrypt_aes_ecb_block(i, k)
        rc = tc ^ tx
        l.append(rc.data)
        tx = i
    d = Data(b"".join(l))
    r = Data(unpad(d.data, 16)) if len(d) % 16 != 0 else d

    return r


def encrypt_aes_cbc(b: Data, k: Data, iv: Data) -> Data:
    d = pkcs7_pad(b, len(b) + (16 - len(b) % 16)) if len(b) % 16 != 0 else b
    l = []
    wb = d.wrap(16)
    tx = iv
    for i in wb:
        tc = i ^ tx
        rc = encrypt_aes_ecb_block(tc, k)
        l.append(rc.data)
        tx = rc
    r = Data(b"".join(l))

    return r


# TODO: Change data to block size
def pkcs7_pad(b: Data, n: int) -> Data:
    bytes_to_add = n - (len(b) % n)
    r = b + Data((b"%c" % bytes_to_add) * bytes_to_add)

    return r
