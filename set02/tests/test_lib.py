from lib import pkcs7pad


def test_pkcs7pad():
    bi = r2 = b"YELLOW SUBMARINE"
    r1 = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    ni1 = 20
    ni2 = 16
    assert pkcs7pad(bi, ni1) == r1 and pkcs7pad(bi, ni2) == r2
