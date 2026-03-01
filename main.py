from bank import BankAccount

def run_test():
    try:
        account = BankAccount("Atheer", 1000)
        print(f"Account Holder: {account.get_account_holder()}")
        print(f"Current Balance: {account.get_balance()}")

        account.deposit(500)
        print(f"Successfully deposited 500. New balance: {account.get_balance()}")

        print("\nAttempting to withdraw 5000...")
        account.withdraw(5000)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_test()