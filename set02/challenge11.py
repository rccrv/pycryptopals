from enum import Enum
# randbytes only works with Python 3.9
# from random import randbytes, randint, random
from random import randint, random, getrandbits

from lib.aes import encryptaescbc, encryptaesecb
from lib.data import Data

def randbytes(n: int) -> bytes:
    return b"".join([b"%c" % getrandbits(8) for i in range(n)])

class AESType(Enum):
    CBC = 1
    EBC = 2

def generate_random_key() -> Data:
    r = Data(randbytes(16))

    return r

def generate_ecb_or_cbc(b: Data, k: Data) -> Data:
    d = Data(randbytes(randint(5, 10)) + b.data + randbytes(randint(5, 10)))
    v = random()
    r = encryptaescbc(d, k, Data(randbytes(16))) if v < 0.5 else encryptaesecb(b, k)
    if v < 0.5:
        print("CBC")
    else:
        print("EBC")
    # r = encryptaescbc(b, k, Data(randbytes(16))) if random() < 0.5 else encryptaesecb(b, k)

    return r

def oracle(d: Data) -> AESType:
    r = AESType.CBC

    print(d.entropy())

    return r

def answer() -> str:
    r = ""
    for i in range(10):
        b = Data(b"YELLOW SUBMARINE")
        k = generate_random_key()
        d = generate_ecb_or_cbc(b, k)
        print(d)
        oracle(d)
        print("-----------------------------------------------")

    return r