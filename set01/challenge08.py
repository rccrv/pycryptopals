from lib.data import Data

# The problem with AES in ECB mode is that when blocks of 16 bytes are equal they will produce
# the same output of 16 bytes. I assumed that the line having the smallest Shannon entropy
# would be the right one given the emphasis the problem statement gives to this information.
#
# The idea is that I to just do a simple calculation instead of doing analysis 16 bytes at a
# time for each line. If you actually print all the entropies, the entropy of line 133 is almost
# 0.5 lower than the next smallest value. Thus it is almost surely our encrypted line.
# def answer() -> str:
#    r = ""
#
#    with open("files/8.txt") as f:
#        line = 1
#        minentropy = float("inf")
#        minline = 1
#
#        for i in f.readlines():
#            d = Data(i.strip(), True)
#            e = d.entropy()
#
#            if e < minentropy:
#                minentropy = e
#                minline = line
#
#            line += 1
#
#        r = f"Line {minline} has the smallest entroty ({minentropy}) and probably was encrypted with AES in ECB mode"
#    return r


def answer() -> str:
    r = ""

    with open("files/8.txt") as f:
        line = 1
        maxscore = 0
        maxline = 1

        for i in f.readlines():
            d = Data(i.strip(), True)
            h = d.wrap(16)
            score = sum([1 if h.count(j) > 1 else 0 for j in h])
            if score > maxscore:
                maxline = line
                maxscore = score

            line += 1

        r = f"Line {maxline} has the highest score ({maxscore}) and probably was encrypted with AES in ECB mode"
    return r
