def bank(Account_Number, Account_Holder_Name, Account_Type, Balance):
    result = {
        f"Account Number": {account_number},
        f"Account Holder Name": {account_holder_name},
        f"Account Type": {account_type},
        f"Balance": {balance}
    }
    return result


if __name__ == "__main__":
    Account_number = 101
    Account_holder_name = "Suraj"
    Account_type = "Savings"
    Balance = 20000

    print(bank(Account_Number, Account_Holder_Name, Account_Type, Balance))
