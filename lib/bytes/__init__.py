from itertools import zip_longest
from math import log2
from typing import List


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


def byteentropy(b: bytes) -> float:
    r = 0.0

    s = set(b)
    v = [b.count(i) / len(b) for i in s]
    v = [i * log2(i) for i in v]
    r = -sum(v)

    return r
