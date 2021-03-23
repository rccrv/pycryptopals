from lib.xor import xor

# from lib.xor import xorrepeatedkey
# from lib.xor import xorsingleletter
#
#
# def test_xorrepeatedkey():
#    sis = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
#    kis = "ICE"
#    rs = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
#    sib = b"ABC"
#    kib = b"ICE"
#    rb = b"\x08\x01\x06"
#    assert xorrepeatedkey(sis, kis) == rs and xorrepeatedkey(sib, kib) == rb


def test_xor():
    sis = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode(
        "utf-8"
    )
    kis = "ICE".encode("utf-8")
    rs = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    sib = b"ABC"
    kib = b"ICE"
    rb = b"\x08\x01\x06"
    sik = bytes.fromhex(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    )
    kik = "X".encode("utf-8")
    rk = "Cooking MC's like a pound of bacon"
    assert (
        xor(sis, kis).hex() == rs
        and xor(sib, kib) == rb
        and xor(sik, kik).decode("utf-8") == rk
    )


# def test_xoredsingleletter():
#    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
#    ki = ord("X")
#    r = "Cooking MC's like a pound of bacon"
#    assert xorsingleletter(si, ki) == r
