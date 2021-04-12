# This will not be necessary after Python 3.10
from __future__ import annotations
from dataclasses import dataclass
from itertools import cycle, zip_longest
from math import log2
from sys import byteorder
from typing import List, Optional, TypeVar

from lib.consts import D


T = TypeVar("T", bytes, str)


@dataclass
class Data:
    data: bytes
    transposed: Optional[List[Data]] = None

    def __init__(self, data: T, hexstring: bool = False):
        if isinstance(data, bytes):
            self.data = data
        elif isinstance(data, str) and hexstring != True:
            self.data = data.encode("utf-8")
        elif isinstance(data, str) and hexstring == True:
            self.data = bytes.fromhex(data)
        else:
            raise TypeError(
                "data should be 'bytes', 'str' or bytes encoded in hex 'str'"
            )

    def __add__(self, other: Data) -> Data:
        r = Data(self.data + other.data)

        return r

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __xor__(self, other: Data) -> Data:
        ls = len(self.data)
        lo = len(other.data)
        if lo < ls:
            z = zip(self.data, cycle(other.data))
        elif ls > lo:
            z = zip(other.data, cycle(self.data))
        else:
            z = zip(self.data, other.data)

        r = Data(b"".join([b"%c" % (i[0] ^ i[1]) for i in z]))
        return r

    def base64(self) -> str:
        r = ""
        for i in range(0, len(self.data), 3):
            n1 = int.from_bytes(self.data[i : i + 1], byteorder)
            n2 = int.from_bytes(self.data[i + 1 : i + 2], byteorder)
            n3 = int.from_bytes(self.data[i + 2 : i + 3], byteorder)
            d1 = (n1 & 0b11111100) >> 2
            d2 = (n1 & 0b00000011) << 4 | (n2 & 0b11110000) >> 4
            d3 = (n2 & 0b00001111) << 2 | (n3 & 0b11000000) >> 6
            d4 = n3 & 0b00111111

            r += f"{D[d1]}{D[d2]}{D[d3]}{D[d4]}"
        return r

    def entropy(self) -> float:
        r = 0.0

        sb = self.data
        s = set(sb)
        v = [sb.count(i) / len(sb) for i in s]
        v = [i * log2(i) for i in v]
        r = -sum(v)

        return r

    def wrap(self, s: int) -> List[Data]:
        b = self.data
        chunks = (
            [Data(b[i : (i + s)]) for i in range(0, len(b), s)]
            if len(b) % s == 0
            else [Data(b[i : (i + s)]) for i in range(0, len(b) - s, s)]
            + [Data(b[len(b) - (len(b) % s) :])]
        )
        return chunks

    def transpose(self, s: int) -> List[Data]:
        chunks = self.wrap(s)
        v = [
            tuple(b"%c" % k for k in i if isinstance(k, int))
            for i in zip_longest(*chunks)
        ]
        self.transposed = [Data(b"".join(i)) for i in v]
        return self.transposed
