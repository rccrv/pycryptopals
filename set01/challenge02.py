def answer() -> str:
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    r = ""

    for i in range(0, len(s1), 2):
        n1 = int("0x" + s1[i : i + 2], 16)
        n2 = int("0x" + s2[i : i + 2], 16)

        n = str(hex(n1 ^ n2))[2:]
        r += f"{n}"

    return r
