import string
from typing import Final, List, Tuple, Dict

from lib import xorsingleletter


class ChiSquare:
    def __init__(self, s: str):
        self.ALPHABET: Final[Dict[str, float]] = {
            "a": 0.08167,
            "b": 0.01492,
            "c": 0.02782,
            "d": 0.04253,
            "e": 0.12702,
            "f": 0.02228,
            "g": 0.02015,
            "h": 0.06094,
            "i": 0.06966,
            "j": 0.00153,
            "k": 0.00772,
            "l": 0.04025,
            "m": 0.02406,
            "n": 0.06749,
            "o": 0.07507,
            "p": 0.01929,
            "q": 0.00095,
            "r": 0.05987,
            "s": 0.06327,
            "t": 0.09056,
            "u": 0.02758,
            "v": 0.00978,
            "w": 0.02360,
            "x": 0.00150,
            "y": 0.01974,
            "z": 0.00074,
        }

        self.__l = (
            list(range(ord("a"), ord("z") + 1))
            + list(range(ord("A"), ord("Z") + 1))
            + list(range(ord(":"), ord("@") + 1))
            + list(range(ord(" "), ord("/") + 1))
            + list(range(ord("0"), ord("9") + 1))
        )

        self.s = s

    def chisquare(self, xored: str) -> float:
        sum = 0.0
        if len(xored) > 0:
            for c in xored:
                if (not c.isascii()) or ord(c) > 128:
                    sum += float("inf")
                elif c.isascii() and c.isalpha():
                    e = self.ALPHABET[c]
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

        for c in self.__l:
            xored = xorsingleletter(self.s, c)

            bn = self.chisquare(xored.lower())

            if bn < bestfit[1]:
                bestfit = (chr(c), bn, xored)
        return bestfit
