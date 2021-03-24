import string
from typing import Tuple

from lib.consts import ALPHABET, CHARS
from lib.data import Data


class ChiSquare:
    def __init__(self, s: str):
        self.s = s
        self.d = Data(s, True)
        self.b = bytes.fromhex(s)

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

    def analysis(self) -> Tuple[str, float, str]:
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
