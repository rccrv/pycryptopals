from base64 import b64decode

from lib.aes import encrypt_aes_ecb, generate_random_key, oracle_aes_ecb_or_cbc
from lib.data import Data


def answer() -> str:
    r = ""
    s = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
    with open("files/12.txt", "rb") as f:
        b_my_string = Data(f.read().strip())
        b_s = Data(b64decode(s))
        b = b_my_string + b_s
        k = generate_random_key()
        #c = encrypt_aes_ecb(b, k)
        # TODO: Idea:
        # 1. As the input is padded using PKCS 7 padding, get the length of the block
        #    by processing the length of the output of repetitions of subsections of my
        #    original string. do that until the block size change. The block size will be
        #    the difference of the last and last but one lengths of output strings.
        #
        # 2. Iterate until the oracle function detect that those repetitions are
        #    encrypted using ECB mode.
        #
        # 3. Follow the next stps on https://cryptopals.com/sets/2/challenges/12
        for i in range(1, 50):
            c = encrypt_aes_ecb(b_my_string[0] * i, k)
            print(len(c))
            print(oracle_aes_ecb_or_cbc(c))

    return r
