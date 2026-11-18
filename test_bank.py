from bank import bankoper

def test_deposit():
    totalBal , UpdatedBal = bankoper(200000, 30000,0)

    assert totalBal == 2300000
    assert UpdatedBal == 230000

def test_withdraw():
    totalBal, upadatedbal = bankoper(100000, 40000 , 10000)

    assert totalBal == 140000
    assert upadatedbal == 130000

def test_anyamount():
    totalBal , updatedBal = bankoper(150000, 0 , 150000)

    assert totalBal == 150000
    assert updatedBal == 135000