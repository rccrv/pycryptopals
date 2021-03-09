from base64 import b64decode

from Crypto.Cipher import AES

def decryptaesebc(b: bytes, k: bytes) -> str:
    cipher = AES.new(k, AES.MODE_ECB)
    r = cipher.decrypt(b).decode('utf-8')
    return r

def answer() -> str:
    key = b"YELLOW SUBMARINE"
    r = ""
    with open('files/7.txt', 'rb') as f:
        bytes = b64decode(f.read())
        r = decryptaesebc(bytes, key)

    return r