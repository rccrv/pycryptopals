from lib.chisquare.extended import ExtendedChiSquare


def answer() -> str:
    r = ""

    with open("files/6.txt") as f:
        content = f.read().strip()
        minsizes = 1
        seq = range(2, 41)

        a = ExtendedChiSquare(content, minsizes, seq)

        s = a.solve()
        r = "".join([f"Candidate key of size {i[0]}\nGot {i[1]}\n\n" for i in s])

    return r.strip()
