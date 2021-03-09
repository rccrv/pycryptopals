from base64 import b64decode
from typing import Dict, List, Iterable, Tuple

from lib import bytestohexstring, hd, transposebytes, wrapbytes
from lib.chisquare import ChiSquare


class Answer(ChiSquare):
    def __init__(self, s: str, sizes: int, seq: Iterable[int]):
        self.bytes = b64decode(s)
        self.indices: List[Tuple[int, int]] = [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),
            (2, 3),
        ]
        self.minsizes = sizes
        self.seq = seq

        self.ALPHABET: Dict[str, float] = {
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

        self.l: List[int] = (
            list(range(ord("a"), ord("z") + 1))
            + list(range(ord("A"), ord("Z") + 1))
            + list(range(ord(":"), ord("@") + 1))
            + list(range(ord(" "), ord("/") + 1))
            + list(range(ord("0"), ord("9") + 1))
        )

        self.s = ""

        self.smallerkeys: List[int] = []

    # TODO: Write unit tests for the 3 functions bellow
    def processkeysize(self, keysize: int) -> float:
        v = [self.bytes[i * keysize : (i + 1) * keysize] for i in range(4)]
        r = [hd(v[i], v[k]) / keysize for i, k in self.indices]
        return sum(r) / len(r)

    def getkeysizes(self) -> List[int]:
        v = map(self.processkeysize, self.seq)
        r = [i[0] for i in sorted(enumerate(v), key=lambda n: n[1])]
        return [list(self.seq)[i] for i in r[: self.minsizes]]

    def solve(self) -> List[Tuple[int, str]]:
        self.smallerkeys = self.getkeysizes()
        r: List[Tuple[int, str]] = []
        for i in self.smallerkeys:
            wb = wrapbytes(self.bytes, i)
            tb = transposebytes(wb)
            k: List[str] = []
            for b in tb:
                self.s = bytestohexstring(b)
                a = self.analysis()
                if a[0] == "\0":
                    k.append("=")
                else:
                    k.append(a[0])
            r.append((i, "".join(k)))
        return r


def answer() -> str:
    r = ""
    with open("files/6.txt") as f:
        content = f.read().strip()
        minsizes = 1
        seq = range(2, 41)
        a = Answer(content, minsizes, seq)
        s = a.solve()
        r = "".join([f"Candidate key of size {i[0]}\nGot {i[1]}\n\n" for i in s])
    return r.strip()
