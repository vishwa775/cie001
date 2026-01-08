def bank(Account_Number, Account_Holder_Name, Account_Type, Balance):
    result = {
        f"Account Number": {Account_Number},
        f"Account Holder Name": {Account_Holder_Name},
        f"Account Type": {Account_Type},
        f"Balance": {Balance}
    }
    return result


if __name__ == "__main__":
    Account_number = 101
    Account_holder_name = "Suraj"
    Account_type = "Savings"
    Balance = 20000

    print(bank(Account_Number, Account_Holder_Name, Account_Type, Balance))
