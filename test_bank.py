from bank import bank

def test_bank():
    expected_output = {
        "Account Number": 101,
        "Account Holder Name": "Suraj",
        "Account Type": "Savings",
        "Balance": 20000
    }

    assert bank(101, "Suraj", "Savings", 20000) == expected_output
