from lib.aes import pkcs7pad
from lib.aes import decryptaesecb
from lib.aes import encryptaesecb


def test_decryptaesecb():
    bi = b"\x9d\xa8\xf5\x85\x07\xd3\x8a\x88\xf5\xdb\xfe\x94\x18\xf6\xa1\x13"
    ki = b"ABCDEFGHIJKLMNOP"
    r = b"0123456789012345"
    assert decryptaesecb(bi, ki) == r


def test_pkcs7pad():
    bi = r2 = b"YELLOW SUBMARINE"
    r1 = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    ni1 = 20
    ni2 = 16
    assert pkcs7pad(bi, ni1) == r1 and pkcs7pad(bi, ni2) == r2


def test_encryptaesecb():
    bi = b"0123456789012345"
    ki = k = b"ABCDEFGHIJKLMNOP"
    r = b"\x9d\xa8\xf5\x85\x07\xd3\x8a\x88\xf5\xdb\xfe\x94\x18\xf6\xa1\x13"
    assert encryptaesecb(bi, ki) == r
