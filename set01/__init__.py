from typing import Optional

from set01 import challenge01
from set01 import challenge02
from set01 import challenge03
from set01 import challenge04
from set01 import challenge05
from set01 import challenge06
from set01 import challenge07
from set01 import challenge08


def challenges(c: Optional[int] = None):
    if c is None:
        print("# cryptopals - set 01 #")
        print("- challenge 01 -")
        print(challenge01.answer())
        print("- challenge 02 -")
        print(challenge02.answer())
        print("- challenge 03 -")
        print(challenge03.answer())
        print("- challenge 04 -")
        print(challenge04.answer())
        print("- challenge 05 -")
        print(challenge05.answer())
        print("- challenge 06 -")
        print(challenge06.answer())
        print("- challenge 07 -")
        print(challenge07.answer())
        print("- challenge 08 -")
        print(challenge08.answer())
    else:
        if c == 1:
            print(challenge01.answer())
        elif c == 2:
            print(challenge02.answer())
        elif c == 3:
            print(challenge03.answer())
        elif c == 4:
            print(challenge04.answer())
        elif c == 5:
            print(challenge05.answer())
        elif c == 6:
            print(challenge06.answer())
        elif c == 7:
            print(challenge07.answer())
        elif c == 8:
            print(challenge08.answer())
