from itertools import cycle
from typing import TypeVar


T = TypeVar("T", str, bytes)


def xor(a: T, b: T) -> T:
    if isinstance(a, str) and isinstance(b, str):
        return b"".join(
            [
                b"%c" % (i[0] ^ i[1])
                for i in zip(a.encode("utf-8"), cycle(b.encode("utf-8")))
            ]
        ).decode("utf-8")
    elif isinstance(a, bytes) and isinstance(b, bytes):
        return b"".join([b"%c" % (i[0] ^ i[1]) for i in zip(a, cycle(b))])
    else:
        raise TypeError("both arguments a and b should be of the same type")
