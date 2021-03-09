from itertools import cycle, zip_longest
from math import log2
from typing import List


def xorrepeatedkey(s: str, key: str) -> str:
    return "".join(f"{ord(z[0]) ^ ord(z[1]):02x}" for z in zip(s, cycle(key)))


def xorsingleletter(s: str, key: int) -> str:
    return "".join([chr(key ^ b) for b in hexstringtobytes(s)])


def popcount(n: int) -> int:
    x = n
    count = 0

    while x > 0:
        count += 1
        x &= x - 1

    return count


def hd(s1: bytes, s2: bytes) -> int:
    return sum([popcount(i[0] ^ i[1]) for i in zip(s1, s2)])


def transposebytes(l: List[bytes]) -> List[bytes]:
    v = [tuple(b"%c" % k for k in i if isinstance(k, int)) for i in zip_longest(*l)]
    r = [b"".join(i) for i in v]
    return r


def wrapbytes(b: bytes, s: int) -> List[bytes]:
    return (
        [b[i : (i + s)] for i in range(0, len(b), s)]
        if len(b) % s == 0
        else [b[i : (i + s)] for i in range(0, len(b) - s, s)]
        + [b[len(b) - (len(b) % s) :]]
    )


def bytestohexstring(b: bytes) -> str:
    return "".join(["{:02x}".format(i) for i in b])


def hexstringtobytes(s: str) -> bytes:
    return bytes([int("0x" + s[i : i + 2], 16) for i in range(0, len(s), 2)])


def byteentropy(b: bytes) -> float:
    r = 0.0

    s = set(b)
    v = [b.count(i) / len(b) for i in s]
    v = [i * log2(i) for i in v]
    r = -sum(v)

    return r
