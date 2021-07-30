from lib.aes import generate_random_key, generate_ecb_or_cbc, oracle_aes_ecb_or_cbc
from lib.data import Data


def answer() -> str:
    r = ""
    with open("files/11.txt", "rb") as f:
        b = Data(f.read().strip())
        k = generate_random_key()
        d = generate_ecb_or_cbc(b, k)
        o = oracle_aes_ecb_or_cbc(d)
        r = f"Data was encrypted using {o[0].value} and has a score of {o[1]}"

    return r
