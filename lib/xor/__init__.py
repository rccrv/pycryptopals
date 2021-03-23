from itertools import cycle
from typing import Generic, TypeVar


T = TypeVar("T", str, bytes)


def xor(a: T, b: T) -> T:
    if isinstance(a, str):
        return b"".join(
            [
                b"%c" % (i[0] ^ i[1])
                for i in zip(a.encode("utf-8"), cycle(b.encode("utf-8")))
            ]
        ).decode("utf-8")
    else:
        return b"".join([b"%c" % (i[0] ^ i[1]) for i in zip(a, cycle(b))])
