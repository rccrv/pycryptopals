from enum import Enum
from random import randbytes, randint, random
from typing import Tuple

from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

from lib.data import Data


class AESType(Enum):
    CBC = "CBC"
    ECB = "ECB"


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


def pkcs7_pad(b: Data, s: int) -> Data:
    bytes_to_add = s - (len(b) % s)
    r = b + Data((b"%c" % bytes_to_add) * bytes_to_add)

    return r


def generate_random_key() -> Data:
    r = Data(randbytes(16))

    return r


def generate_ecb_or_cbc(b: Data, k: Data) -> Data:
    d = Data(randbytes(randint(5, 10))) + b + Data(randbytes(randint(5, 10)))
    v = random()
    r = encrypt_aes_cbc(d, k, Data(randbytes(16))) if v < 0.5 else encrypt_aes_ecb(d, k)

    return r


def oracle_aes_ecb_or_cbc(d: Data) -> Tuple[AESType, int]:
    r = ()  # type: ignore

    h = d.wrap(16)
    score = len(h) - len(set(h))
    r = (AESType.ECB, score) if score > 0 else (AESType.CBC, score)  # type: ignore

    return r  # type: ignore
