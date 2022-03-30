from lib.bytes import popcount
from lib.bytes import hd


def test_popcount():
    i = 11
    r = 3
    assert popcount(i) == r


def test_hd():
    s1i = "this is a test".encode("utf-8")
    s2i = "wokka wokka!!!".encode("utf-8")
    r = 37
    assert hd(s1i, s2i) == r
