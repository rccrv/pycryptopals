from lib.chisquare import ChiSquare


class Answer(ChiSquare):
    pass


def answer() -> str:
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    a = Answer(s)
    r = a.analysis()

    return f"Decoded by using '{r[0]}'\nResult: {r[2]}"
