import itertools


def xorrepeatedkey(s: str, key: str):
    cycle = itertools.cycle(key)
    r = "".join(f"{ord(z[0]) ^ ord(z[1]):02x}" for z in zip(s, cycle))

    return r
