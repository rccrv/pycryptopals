from Crypto.Cipher import AES

from lib.aes import pkcs7pad
from lib.aes import decryptaesecbblock
from lib.aes import encryptaesecbblock
from lib.aes import decryptaesecb
from lib.aes import encryptaesecb
from lib.aes import decryptaescbc
from lib.aes import encryptaescbc
from lib.data import Data


def test_pkcs7pad():
    bi = r2 = Data(b"YELLOW SUBMARINE")
    r1 = Data(b"YELLOW SUBMARINE\x04\x04\x04\x04")
    ni1 = 20
    ni2 = 16
    assert pkcs7pad(bi, ni1) == r1 and pkcs7pad(bi, ni2) == r2


def test_decryptaesecbblock():
    bi = Data(b"\x9d\xa8\xf5\x85\x07\xd3\x8a\x88\xf5\xdb\xfe\x94\x18\xf6\xa1\x13")
    ki = Data(b"ABCDEFGHIJKLMNOP")
    r = Data(b"0123456789012345")
    assert decryptaesecbblock(bi, ki) == r


def test_encryptaesecbblock():
    bi = Data(b"0123456789012345")
    ki = Data(b"ABCDEFGHIJKLMNOP")
    r = Data(b"\x9d\xa8\xf5\x85\x07\xd3\x8a\x88\xf5\xdb\xfe\x94\x18\xf6\xa1\x13")
    assert encryptaesecbblock(bi, ki) == r


def test_decryptaesecb():
    bi = Data(b'\x9d\xa8\xf5\x85\x07\xd3\x8a\x88\xf5\xdb\xfe\x94\x18\xf6\xa1\x13\xf6\x12\x77\xea\x63\xd6\x8a\x1f\x3f\xb6\xef\x2a\x02\x60\xc4\x78')
    ki = Data(b"ABCDEFGHIJKLMNOP")
    r = Data(b"01234567890123456")
    assert decryptaesecb(bi, ki) == r


def test_encryptaesecb():
    bi = Data(b"01234567890123456")
    ki = Data(b"ABCDEFGHIJKLMNOP")
    r = Data(b'\x9d\xa8\xf5\x85\x07\xd3\x8a\x88\xf5\xdb\xfe\x94\x18\xf6\xa1\x13\xf6\x12\x77\xea\x63\xd6\x8a\x1f\x3f\xb6\xef\x2a\x02\x60\xc4\x78')
    assert encryptaesecb(bi, ki) == r


# TODO: CBC doesn't work with padded data
def test_decryptaescbc():
    bi = Data(b"AAAABBBBCCCCDDDD" * 2)
    iv = Data(b"\x00" * 16)
    ki = Data(b"YELLOW SUBMARINE")
    cipher = AES.new(ki.data, AES.MODE_CBC, iv=iv.data)
    encrypted = encryptaescbc(bi, ki, iv)
    assert cipher.decrypt(encrypted.data) == decryptaescbc(encrypted, ki, iv).data


def test_encryptaescbc():
    bi = Data(b"AAAABBBBCCCCDDDD" * 2)
    iv = Data(b"\x00" * 16)
    ki = Data(b"YELLOW SUBMARINE")
    cipher = AES.new(ki.data, AES.MODE_CBC, iv=iv.data)
    encrypted = encryptaescbc(bi, ki, iv)
    assert cipher.encrypt(bi.data) == encrypted.data
