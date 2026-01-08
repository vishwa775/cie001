def bank(account_number, account_holder_name, account_type, balance):
    result = {
        f"Account Number": {account_number},
        f"Account Holder Name": {account_holder_name},
        f"Account Type": {account_type},
        f"Balance": {balance}
    }
    return result


if __name__ == "__main__":
    account_number = 101
    account_holder_name = "Suraj"
    account_type = "Savings"
    balance = 20000

    print(bank(account_number, account_holder_name, account_type, balance))
