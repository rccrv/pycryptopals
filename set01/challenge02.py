from lib.data import Data

def answer() -> str:
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    d1 = Data(s1, True)
    d2 = Data(s2, True)
    r = (d1 ^ d2).data.hex()

    return r
