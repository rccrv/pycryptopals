# TODO: This should go to a function
def answer() -> str:
    d = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    r = ""

    for i in range(0, len(s), 6):
        n1 = int(s[i : i + 2], 16)
        n2 = int(s[i + 2 : i + 4], 16)
        n3 = int(s[i + 4 : i + 6], 16)
        d1 = (n1 & 0b11111100) >> 2
        d2 = (n1 & 0b00000011) << 4 | (n2 & 0b11110000) >> 4
        d3 = (n2 & 0b00001111) << 2 | (n3 & 0b11000000) >> 6
        d4 = n3 & 0b00111111

        r += f"{d[d1]}{d[d2]}{d[d3]}{d[d4]}"

    return r
