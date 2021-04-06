from pytest import approx

from lib.chisquare.extended import ExtendedChiSquare
from lib.data import Data


def test_ExtendedChisquare_processkeysize():
    si = "GRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VoY1N0AwwKbRBzaxERCHlwBwQQA3l0Dh0NbWsOQRERBAoAAhZ5GRFlaxUVDBBuaxEcFQ0AeGtTGRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VtY1si"
    mini = 1
    seqi = range(2, 20)
    al = [3.25, 3.2222222222222228, 3.2916666666666665, 2.966666666666667, 2.694444444444444, 3.4523809523809526, 3.6041666666666665, 2.907407407407407, 3.25, 3.6363636363636367, 3.0833333333333335, 3.1153846153846154, 3.5238095238095237, 3.3444444444444446, 3.3229166666666665, 3.392156862745098, 2.842592592592593, 3.3947368421052633]
    rl = [approx(i) for i in al]
    to = ExtendedChiSquare(si, mini, seqi)
    assert rl == [to.processkeysize(i) for i in seqi]

def test_ExtendedChisquare_getkeysizes():
    si = "GRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VoY1N0AwwKbRBzaxERCHlwBwQQA3l0Dh0NbWsOQRERBAoAAhZ5GRFlaxUVDBBuaxEcFQ0AeGtTGRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VtY1si"
    mini = 1
    seqi = range(2, 20)
    to = ExtendedChiSquare(si, mini, seqi)
    assert to.getkeysizes() == [6]

# TODO: Getting gibberish instead of "MY KEY"
# def test_ExtendedChisquare_solve():
#     si = "GRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VoY1N0AwwKbRBzaxERCHlwBwQQA3l0Dh0NbWsOQRERBAoAAhZ5GRFlaxUVDBBuaxEcFQ0AeGtTGRFpGGUQHnl0AwB5HRVhAgt5GRx4H2VtY1si"
#     mini = 1
#     seqi = range(2, 7)
#     to = ExtendedChiSquare(si, mini, seqi)
#     s = to.solve()
#     print(s)
#     ciphertext = Data(b64decode(si))