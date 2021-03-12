from pytest import approx

from lib import (
    byteentropy,
    xorrepeatedkey,
    xorsingleletter,
    popcount,
    hd,
    transposebytes,
    wrapbytes,
    bytestohexstring,
    hexstringtobytes,
    byteentropy,
    decryptaesecb,
)
from lib.chisquare import ChiSquare


def test_xorrepeatedkey():
    si = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    ki = "ICE"
    r = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    assert xorrepeatedkey(si, ki) == r


def test_xoredsingleletter():
    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ki = ord("X")
    r = "Cooking MC's like a pound of bacon"
    assert xorsingleletter(si, ki) == r


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


def test_bytestohexstring():
    bi = b"AA\x02"
    r = "414102"
    assert bytestohexstring(bi) == r


def test_hexstringtobytes():
    si = "414102"
    r = b"AA\x02"
    assert hexstringtobytes(si) == r


def test_byteentropy():
    bi = b"AA\x02"
    r = approx(0.91829583)
    assert byteentropy(bi) == r


def test_decryptaesecb():
    bi = b"\x9d\xa8\xf5\x85\x07\xd3\x8a\x88\xf5\xdb\xfe\x94\x18\xf6\xa1\x13"
    ki = b"ABCDEFGHIJKLMNOP"
    r = b"0123456789012345"
    assert decryptaesecb(bi, ki) == r


def test_Chisequare_chisquare():
    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ki = "X"
    to = ChiSquare(si)
    ixored = xorsingleletter(si, ord(ki)).lower()
    r = approx(1001.7714498)
    assert to.chisquare(ixored) == r


def test_Chisequare_analysis():
    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    to = ChiSquare(si)
    r = ("X", approx(1001.7714498), "Cooking MC's like a pound of bacon")
    assert to.analysis() == r
