# This will not be necessary after Python 3.10
from __future__ import annotations
from dataclasses import dataclass
from itertools import cycle, zip_longest
from sys import byteorder
from typing import List, Optional, Sequence, TypeVar, Union

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

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other: object):
        return self.data == other.data if isinstance(other, Data) else False

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

    def __getitem__(
        self, item: Union[int, slice]
    ) -> Union[Data, Sequence[Data, None, None]]:  # type: ignore
        if isinstance(item, int):
            return Data(b"%c" % self.data[item])
        elif isinstance(item, slice):
            return Data(self.data[item])
        else:
            raise TypeError("subscriptable index shoult be an integer or an slice")

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

    def wrap(self, s: int) -> List[Data]:
        chunks = (
            [self[i : (i + s)] for i in range(0, len(self), s)]
            if len(self) % s == 0
            else [self[i : (i + s)] for i in range(0, len(self) - s, s)]
            + [self[len(self) - (len(self) % s) :]]
        )

        return chunks  # type: ignore

    def transpose(self, s: int) -> List[Data]:
        chunks = self.wrap(s)
        v = [
            tuple(b"%c" % k for k in i if isinstance(k, int))
            for i in zip_longest(*chunks)
        ]
        self.transposed = [Data(b"".join(i)) for i in v]
        return self.transposed
