from base64 import b64decode
from typing import Iterable, List, Tuple

from lib.bytes import hd
from lib.chisquare import ChiSquare
from lib.consts import INDICES
from lib.data import Data
from lib.data.extended import ExtendedData


class ExtendedChiSquare(ChiSquare):
    def __init__(self, s: str, sizes: int, seq: Iterable[int]):
        self.data = ExtendedData(b64decode(s))
        self.minsizes = sizes
        self.seq = seq

        self.d = Data(b"\x00")
        self.smallerkeys: List[int] = []

    # TODO: Write unit tests for the 3 methods bellow.
    def processkeysize(self, keysize: int) -> float:
        db = self.data.data
        v = [db[i * keysize : (i + 1) * keysize] for i in range(4)]
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
            tb = self.data.transpose(i)
            k: List[str] = []

            for b in tb:
                self.d = b
                a = self.analysis()
                k.append(a[0])

            r.append((i, "".join(k)))
        return r
