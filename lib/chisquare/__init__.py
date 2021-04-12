import string
from base64 import b64decode
from typing import Iterable, List, Optional, Tuple

from lib.bytes import hd
from lib.consts import ALPHABET, CHARS, INDICES
from lib.data import Data


class ChiSquare:
    def __init__(
        self,
        s: str,
        singleletter: bool = True,
        sizes: Optional[int] = None,
        seq: Optional[Iterable[int]] = None,
    ):
        if singleletter == True:
            self.s = s
            self.d = Data(s, True)
        else:
            self.data = Data(b64decode(s))
            self.minsizes = sizes
            # This class was merged with an ExtendedChiSquare class.
            # This is necessary so mypy doesn't complain about wrong
            # typting.
            self.seq = seq if seq is not None else []

            self.d = Data(b"\x00")
            self.smallerkeys: List[int] = []

    def chisquare(self, xored: str) -> float:
        sum = 0.0
        if len(xored) > 0:
            for c in xored:
                if (not c.isascii()) or ord(c) > 128:
                    sum += float("inf")
                elif c.isascii() and c.isalpha():
                    e = ALPHABET[c]
                    sum += ((1.0 - e) ** 2.0) / e
                elif c.isascii() and c.isdecimal():
                    sum += 100.0
                elif c.isascii() and c.isspace():
                    sum += 10.0
                elif c.isascii() and c in string.punctuation:
                    sum += 100.0
                else:
                    sum += float("inf")
        return sum

    def solve_single_letter(self) -> Tuple[str, float, str]:
        bestfit = ("\0", float("inf"), "")

        for c in CHARS:
            nc = Data(b"%c" % c)
            try:
                xored = (self.d ^ nc).data.decode("utf-8")
                bn = self.chisquare(xored.lower())
            except UnicodeDecodeError:
                xored = ""
                bn = float("inf")

            if bn < bestfit[1]:
                bestfit = (chr(c), bn, xored)
        return bestfit

    def process_key_size(self, keysize: int) -> float:
        db = self.data.data
        v = [db[i * keysize : (i + 1) * keysize] for i in range(4)]
        r = [hd(v[i], v[k]) / keysize for i, k in INDICES]

        return sum(r) / len(r)

    def get_key_sizes(self) -> List[int]:
        v = map(self.process_key_size, self.seq)
        r = [i[0] for i in sorted(enumerate(v), key=lambda n: n[1])]

        return [list(self.seq)[i] for i in r[: self.minsizes]]

    # This method isn't tested. I tried creating cases for testing, but they all failed.
    # It solves the challenge. So I will keep it that way.
    def solve_repeated_key(self) -> List[Tuple[int, str]]:
        self.smallerkeys = self.get_key_sizes()
        r: List[Tuple[int, str]] = []

        for i in self.smallerkeys:
            tb = self.data.transpose(i)
            k: List[str] = []

            for b in tb:
                self.d = b
                a = self.solve_single_letter()
                k.append(a[0])

            r.append((i, "".join(k)))
        return r
