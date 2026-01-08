from bank import bank_details

def test_bank_details():
    expected_output = {
        "Account Number": 101,
        "Account Holder Name": "Suraj",
        "Account Type": "Savings",
        "Balance": 20000
    }

    assert bank_details(101, "Suraj", "Savings", 20000) == expected_output
