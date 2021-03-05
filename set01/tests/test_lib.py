from pytest import approx

from lib import xorrepeatedkey, xorsingleletter, s2b, popcount, hd
from lib.chisquare import ChiSquare


def test_xorrepeatedkey():
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    k = "ICE"
    assert (
        xorrepeatedkey(s, k)
        == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
)


def test_xoredsingleletter():
    s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    k = ord("X")
    assert xorsingleletter(s1, k) == "Cooking MC's like a pound of bacon"


def test_s2b():
    assert s2b("A") == [10]


def test_popcount():
    n3 = 11
    assert popcount(n3) == 3


def test_hd():
    s1 = "this is a test"
    s2 = "wokka wokka!!!"
    assert hd(s1, s2) == 37


def test_s2b():
    assert s2b("A") == [10]


def test_Chisequare_chisquare():
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    c = ChiSquare(s)
    xored = xorsingleletter(s, ord("X"))
    assert c.chisquare(xored.lower()) == approx(1001.7714498)


def test_Chisequare_analysis():
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    c = ChiSquare(s)
    assert c.analysis() == (
        "X",
        approx(1001.7714498),
        "Cooking MC's like a pound of bacon",
    )
