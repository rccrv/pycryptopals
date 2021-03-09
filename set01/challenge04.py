from lib.chisquare import ChiSquare


class Answer(ChiSquare):
    pass


def answer():
    bestfit = ("\0", float("inf"), "", 0)
    line = 1

    with open("files/4.txt") as f:
        for s in f.readlines():
            a = Answer(s.strip())
            r = a.analysis()

            if r[1] < bestfit[1]:
                bestfit = (r[0], r[1], r[2], line)

            line += 1

    return f"Decoded line {bestfit[3]} by using '{bestfit[0]}'\nResult: {bestfit[2]}"
