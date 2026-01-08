from bank import bank

def test_bank():
    expected_output = {
        f"account_Number":101,
        f"account_Holder_Name":"Suraj",
        f"account_Type":"Savings",
        f"balance":20000
    }

    assert bank(101,"Suraj","Savings",20000)==expected_output
