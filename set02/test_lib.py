from lib import pkcs7pad


def test_pkcs7pad():
    bi = b"YELLOW SUBMARINE"
    ni = 20
    assert pkcs7pad(bi, ni) == b"YELLOW SUBMARINE\x04\x04\x04\x04"