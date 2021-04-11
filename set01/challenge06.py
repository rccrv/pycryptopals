from lib.chisquare import ChiSquare


def answer() -> str:
    r = ""

    with open("files/6.txt") as f:
        content = f.read().strip()
        minsizes = 1
        seq = range(2, 41)

        a = ChiSquare(content, False, minsizes, seq)

        s = a.solve_repeated_key()
        r = "".join([f"Candidate key of size {i[0]}\nGot {i[1]}\n\n" for i in s])

    return r.strip()
