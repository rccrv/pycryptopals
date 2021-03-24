from lib.data import Data


def answer() -> str:
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    ds = Data(s)
    dk = Data(key)

    return (ds ^ dk).data.hex()
