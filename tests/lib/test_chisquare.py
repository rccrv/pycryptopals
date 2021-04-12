from pytest import approx

from lib.chisquare import ChiSquare
from lib.data import Data


def test_Chisequare_chisquare():
    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ki = "X"
    to = ChiSquare(si)
    ixored = (Data(si, True) ^ Data(ki)).data.decode("utf-8").lower()
    r = approx(1001.7714498)
    assert to.chisquare(ixored) == r


def test_Chisequare_solve_single_letter():
    si = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    to = ChiSquare(si)
    r = ("X", approx(1001.7714498), "Cooking MC's like a pound of bacon")
    assert to.solve_single_letter() == r


def test_Chisquare_process_key_size():
    si = "GRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VoY1N0AwwKbRBzaxERCHlwBwQQA3l0Dh0NbWsOQRERBAoAAhZ5GRFlaxUVDBBuaxEcFQ0AeGtTGRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VtY1si"
    mini = 1
    seqi = range(2, 20)
    al = [
        3.25,
        3.2222222222222228,
        3.2916666666666665,
        2.966666666666667,
        2.694444444444444,
        3.4523809523809526,
        3.6041666666666665,
        2.907407407407407,
        3.25,
        3.6363636363636367,
        3.0833333333333335,
        3.1153846153846154,
        3.5238095238095237,
        3.3444444444444446,
        3.3229166666666665,
        3.392156862745098,
        2.842592592592593,
        3.3947368421052633,
    ]
    rl = [approx(i) for i in al]
    to = ChiSquare(si, False, mini, seqi)
    assert rl == [to.process_key_size(i) for i in seqi]


def test_Chisquare_get_key_sizes():
    si = "GRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VoY1N0AwwKbRBzaxERCHlwBwQQA3l0Dh0NbWsOQRERBAoAAhZ5GRFlaxUVDBBuaxEcFQ0AeGtTGRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VtY1si"
    mini = 1
    seqi = range(2, 20)
    to = ChiSquare(si, False, mini, seqi)
    assert to.get_key_sizes() == [6]
