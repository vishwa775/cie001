def bank(account_Number,account_Holder_Name,account_Type,balance):
    result = {
        f"account_Number": Account_Number,
        f"account_Holder_Name": Account_Holder_Name,
        f"account_Type": Account_Type,
        f"balance": Balance
    }
    return result


if __name__ == "__main__":
    account_Number = 101
    account_Holder_Name = "Suraj"
    account_Type = "Savings"
    balance = 20000

    print(bank(account_Number,account_Holder_Name,account_Type,balance))
