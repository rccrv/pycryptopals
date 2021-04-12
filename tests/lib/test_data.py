from sys import byteorder
from pytest import approx

from lib.data import Data


def test_Data_add():
    d1 = Data(b"\xff")
    d2 = Data(b"\x00")
    r = Data(b"\xff\x00")
    assert d1 + d2 == r


def test_Data_iter():
    d = Data(b"\xff\x00")
    assert [int.from_bytes(b"\xff", byteorder), int.from_bytes(b"\x00", byteorder)] == [
        i for i in d
    ]


def test_Data_len():
    d = Data(b"\xff\x00")
    assert len(d) == 2


def test_Data_xor():
    d1 = Data(b"\xff")
    d2 = Data(b"\x00")
    d3 = Data(b"\xc0\xc0\xc0")
    d4 = Data(b"\xe1\x04\xac")
    r1 = Data(b"\xff")
    r2 = Data(b"!\xc4l")
    assert (d1 ^ d2 == r1) and (d3 ^ d4 == r2)


def test_Data_base64():
    d = Data(b"\xffABC\xd0")
    assert d.base64() == "/0FCQ9AA"


def test_Data_entropy():
    d = Data(b"\xffABC\xd0")
    assert d.entropy() == approx(2.3219280)


def test_Data_wrap():
    d = Data(b"\xffABC\xd0")
    assert d.wrap(3) == [Data(b"\xffAB"), Data(b"C\xd0")]


def test_Data_transpose():
    d = Data(b"\xffABC\xd0")
    assert d.transpose(3) == [Data(b"\xffC"), Data(b"A\xd0"), Data(b"B")]
