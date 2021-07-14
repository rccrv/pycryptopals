from enum import Enum
from random import randbytes, randint, random
from typing import Tuple

from lib.aes import encrypt_aes_cbc, encrypt_aes_ecb
from lib.data import Data


class AESType(Enum):
    CBC = "CBC"
    EBC = "EBC"


def generate_random_key() -> Data:
    r = Data(randbytes(16))

    return r


def generate_ecb_or_cbc(b: Data, k: Data) -> Data:
    d = Data(randbytes(randint(5, 10))) + b + Data(randbytes(randint(5, 10)))
    v = random()
    r = encrypt_aes_cbc(d, k, Data(randbytes(16))) if v < 0.5 else encrypt_aes_ecb(d, k)

    return r


def oracle(d: Data) -> Tuple[AESType, int]:
    r = ()  # type: ignore

    h = d.wrap(16)
    score = len(h) - len(set(h))
    r = (AESType.EBC, score) if score > 0 else (AESType.CBC, score)  # type: ignore

    return r  # type: ignore


def answer() -> str:
    r = ""
    with open("files/11.txt", "rb") as f:
        b = Data(f.read().strip())
        k = generate_random_key()
        d = generate_ecb_or_cbc(b, k)
        o = oracle(d)
        r = f"Data was encrypted using {o[0].value} and has a score of {o[1]}"

    return r
