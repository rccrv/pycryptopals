from typing import Optional

from set02 import challenge09
from set02 import challenge10
from set02 import challenge11


def challenges(c: Optional[int] = None):
    print("# cryptopals - set 02 #")
    if c is None:
        print("- challenge 09 -")
        print(challenge09.answer())
        print("- challenge 10 -")
        print(challenge10.answer())
        print("- challenge 11 -")
        print(challenge11.answer())
    else:
        if c == 9:
            print("- challenge 09 -")
            print(challenge09.answer())
        elif c == 10:
            print("- challenge 10 -")
            print(challenge10.answer())
        elif c == 11:
            print("- challenge 11 -")
            print(challenge11.answer())
