from pytest import approx

from lib.bytes import popcount
from lib.bytes import hd
from lib.bytes import transposebytes
from lib.bytes import wrapbytes
from lib.bytes import byteentropy


def test_popcount():
    i = 11
    r = 3
    assert popcount(i) == r


def test_hd():
    s1i = "this is a test".encode("utf-8")
    s2i = "wokka wokka!!!".encode("utf-8")
    r = 37
    assert hd(s1i, s2i) == r


def test_transposebytes():
    i = [b"a1a2a3a4", b"1b2b3b4b", b"c9c8"]
    r = [b"a1c", b"1b9", b"a2c", b"2b8", b"a3", b"3b", b"a4", b"4b"]
    assert transposebytes(i) == r


def test_wrapbytes():
    bi = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s1i = 2
    s2i = 3
    s3i = 13
    r1i = [
        b"AB",
        b"CD",
        b"EF",
        b"GH",
        b"IJ",
        b"KL",
        b"MN",
        b"OP",
        b"QR",
        b"ST",
        b"UV",
        b"WX",
        b"YZ",
    ]
    r2i = [b"ABC", b"DEF", b"GHI", b"JKL", b"MNO", b"PQR", b"STU", b"VWX", b"YZ"]
    r3i = [b"ABCDEFGHIJKLM", b"NOPQRSTUVWXYZ"]
    assert (
        wrapbytes(bi, s1i) == r1i
        and wrapbytes(bi, s2i) == r2i
        and wrapbytes(bi, s3i) == r3i
    )


def test_byteentropy():
    bi = b"AA\x02"
    r = approx(0.91829583)
    assert byteentropy(bi) == r
