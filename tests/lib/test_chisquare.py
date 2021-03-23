from pytest import approx

from lib.xor import xor

from lib.chisquare import ChiSquare


def test_Chisequare_chisquare():
    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ki = "X"
    to = ChiSquare(si)
    ixored = xor(bytes.fromhex(si), ki.encode("utf-8")).decode("utf-8").lower()
    r = approx(1001.7714498)
    assert to.chisquare(ixored) == r


def test_Chisequare_analysis():
    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    to = ChiSquare(si)
    r = ("X", approx(1001.7714498), "Cooking MC's like a pound of bacon")
    assert to.analysis() == r
