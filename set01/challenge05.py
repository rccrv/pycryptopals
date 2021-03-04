from lib import xorrepeatedkey


def answer() -> str:
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"

    return xorrepeatedkey(s, key)
