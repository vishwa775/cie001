def bank(Account_Number, Account_Holder_Name, Account_Type, Balance):
    result = {
        f"Account Number": {Account_Number}/n,
        f"Account Holder Name": {Account_Holder_Name}/n,
        f"Account Type": {Account_Type}/n,
        f"Balance": {Balance}/n
    }
    return result


if __name__ == "__main__":
    Account_Number = 101
    Account_Holder_Name = "Suraj"
    Account_Type = "Savings"
    Balance = 20000

    print(bank(Account_Number, Account_Holder_Name, Account_Type, Balance))
