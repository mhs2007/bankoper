
from bank import bankoper

def test_deposit():
    totalBal, UpdatedBal = bankoper(200000, 30000, 0)

    assert totalBal == 230000
    assert UpdatedBal == 230000

def test_withdraw():
    totalBal, UpdatedBal = bankoper(100000, 40000, 10000)

    assert totalBal == 140000
    assert UpdatedBal == 130000

def test_anyamount():
    totalBal, UpdatedBal = bankoper(150000, 0, 15000)

    assert totalBal == 150000
    assert UpdatedBal == 135000
