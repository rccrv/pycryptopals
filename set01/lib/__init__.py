import itertools

from typing import List


def xorrepeatedkey(s: str, key: str) -> str:
    cycle = itertools.cycle(key)
    r = "".join(f"{ord(z[0]) ^ ord(z[1]):02x}" for z in zip(s, cycle))

    return r

def s2b(s: str) -> List[int]:
    return [int("0x" + s[i : i + 2], 16) for i in range(0, len(s), 2)]


def xorsingleletter(s: str, key: int) -> str:
    return "".join([chr(key ^ b) for b in s2b(s)])


def popcount(n: int) -> int:
    x = n
    count = 0

    while x > 0:
        count += 1
        x &= x - 1

    return count


def hd(s1: str, s2: str) -> int:
    d = 0
    d = sum([popcount(ord(i[0]) ^ ord(i[1])) for i in zip(s1, s2)])

    return d
