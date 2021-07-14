from enum import Enum

# randbytes only works with Python 3.9
from random import randbytes, randint, random

from lib.aes import encrypt_aes_cbc, encrypt_aes_ecb
from lib.data import Data


class AESType(Enum):
    CBC = 1
    EBC = 2


def generate_random_key() -> Data:
    r = Data(randbytes(16))

    return r


def generate_ecb_or_cbc(b: Data, k: Data) -> Data:
    # TODO: Maybe take this away and change b"A" to a random byte.
    d = Data(b"A" * randint(5, 10)) + b + Data(b"A" * randint(5, 10))
    v = random()
    r = encrypt_aes_cbc(d, k, Data(randbytes(16))) if v < 0.5 else encrypt_aes_ecb(d, k)
    if v < 0.5:
        print("CBC")
    else:
        print("EBC")

    return r


# This works against a large-ish text file and by using the test data repeated a hundred times.
def oracle(d: Data) -> AESType:
    r = AESType.CBC

    h = d.wrap(16)
    score = sum([1 if h.count(j) > 1 else 0 for j in h])
    print(score)
    if score > 0:
        r = AESType.EBC

    return r


def answer() -> str:
    r = ""
    with open("files/11.txt", "rb") as f:
        b = Data(f.read().strip())
        k = generate_random_key()
        d = generate_ecb_or_cbc(b, k)
        o = oracle(d)
        if o == AESType.CBC:
            print("CBC")
        else:
            print("EBC")
    #for i in range(10):
    #    b = Data(
    #        b"YELLOW SUBMARINE1, yellow submarine2, YELLOW SUBMARINE3, yellow submarine4, YELLOW SUBMARINE5, yellow submarine6" * 100
    #    )
    #    k = generate_random_key()
    #    d = generate_ecb_or_cbc(b, k)
    #    o = oracle(d)
    #    if o == AESType.CBC:
    #        print("CBC")
    #    else:
    #        print("EBC")
    #    print("-----------------------------------------------")

    return r
