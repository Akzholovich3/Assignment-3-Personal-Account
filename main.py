from personal_account import PersonalAccount


def test_account():
    account = PersonalAccount(account_number=123456, account_holder="Kamchy")

    account.deposit(600)
    print(account)

    account.withdraw(300)
    print(account)

    account.withdraw(400)
    print(account)

    print(f"Current balance: {account.get_balance()}")

    account.print_transaction_history()


if __name__ == "__main__":
    test_account()