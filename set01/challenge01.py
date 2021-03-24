from lib.data import Data

def answer() -> str:
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    d = Data(s, True)
    r = d.base64()
    return r
