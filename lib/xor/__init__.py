from itertools import cycle

from lib.bytes import hexstringtobytes


def xorrepeatedkey(s: str, key: str) -> str:
    return "".join(f"{ord(z[0]) ^ ord(z[1]):02x}" for z in zip(s, cycle(key)))


def xorsingleletter(s: str, key: int) -> str:
    return "".join([chr(key ^ b) for b in hexstringtobytes(s)])
