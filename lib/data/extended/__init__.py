from dataclasses import dataclass, field
from itertools import zip_longest
from typing import List

from lib.data import Data


@dataclass
class ExtendedData(Data):
    transposed: List[Data] = field(default_factory=list)

    def transpose(self, s: int) -> List[Data]:
        chunks = self.wrap(s)
        v = [
            tuple(b"%c" % k for k in i if isinstance(k, int))
            for i in zip_longest(*chunks)
        ]
        self.transposed = [Data(b"".join(i)) for i in v]
        return self.transposed
