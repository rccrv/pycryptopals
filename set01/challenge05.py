from lib.xor import xor


def answer() -> str:
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"

    return xor(s.encode("utf-8"), key.encode("utf-8")).hex()
