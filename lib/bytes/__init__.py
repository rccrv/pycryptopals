# Python 3.10 will have a int.bit_count()
def popcount(n: int) -> int:
    x = n
    count = 0

    while x > 0:
        count += 1
        x &= x - 1

    return count


def hd(s1: bytes, s2: bytes) -> int:
    return sum([popcount(i[0] ^ i[1]) for i in zip(s1, s2)])
