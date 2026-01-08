from bank import bank

def test_bank():
    expected_output = {
        "Account_Number": 101,
        "Account_Holder_Name": "Suraj",
        "Account_Type": "Savings",
        "Balance": 20000
    }

    assert bank(101, "Suraj", "Savings", 20000) == expected_output
