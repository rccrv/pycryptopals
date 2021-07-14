from lib.data import Data


def answer() -> str:
    r = ""

    with open("files/8.txt") as f:
        line = 1
        maxscore = 0
        maxline = 1

        for i in f.readlines():
            d = Data(i.strip(), True)
            h = d.wrap(16)
            score = len(h) - len(set(h))
            if score > maxscore:
                maxline = line
                maxscore = score

            line += 1

        r = f"Line {maxline} has the highest score ({maxscore}) and probably was encrypted with AES in ECB mode"
    return r
