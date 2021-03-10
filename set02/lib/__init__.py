def pkcs7pad(b: bytes, n: int) -> bytes:
    r = b + (b"%c" % (n - len(b)) * (n - len(b))) if n > len(b) and n <= 255  else 0

    return r