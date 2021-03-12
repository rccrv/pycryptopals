from base64 import b64decode
from typing import List, Iterable, Tuple

from lib.bytes import bytestohexstring, hd, transposebytes, wrapbytes
from lib.chisquare import ChiSquare
from lib.consts import INDICES


class Answer(ChiSquare):
    def __init__(self, s: str, sizes: int, seq: Iterable[int]):
        self.bytes = b64decode(s)
        self.minsizes = sizes
        self.seq = seq

        self.s = ""
        self.smallerkeys: List[int] = []

    # TODO: Write unit tests for the 3 functions bellow. Problably will need to create a mock object
    def processkeysize(self, keysize: int) -> float:
        v = [self.bytes[i * keysize : (i + 1) * keysize] for i in range(4)]
        r = [hd(v[i], v[k]) / keysize for i, k in INDICES]

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
