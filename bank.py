def bank(Account_Number, Account_Holder_Name, Account_Type, Balance):
    result = {
        f"Account_Number": Account_Number,
        f"Account_Holder Name": Account_Holder_Name,
        f"Account_Type": Account_Type,
        f"Balance": Balance
    }
    return result


if __name__ == "__main__":
    Account_Number = 101
    Account_Holder_Name = "Suraj"
    Account_Type = "Savings"
    Balance = 20000

    print(bank(Account_Number, Account_Holder_Name, Account_Type, Balance))
