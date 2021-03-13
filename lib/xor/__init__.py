from itertools import cycle
from typing import Generic, TypeVar

from lib.bytes import hexstringtobytes


T = TypeVar("T", str, bytes)

def xorrepeatedkey(s: T, key: T) -> T:
    if isinstance(s, str):
        return "".join(f"{ord(z[0]) ^ ord(z[1]):02x}" for z in zip(s, cycle(key)))
    else:
        return b"".join([b"%c" % (z[0] ^ z[1]) for z in zip(s, cycle(key))])


def xorsingleletter(s: str, key: int) -> str:
    return "".join([chr(key ^ b) for b in hexstringtobytes(s)])
