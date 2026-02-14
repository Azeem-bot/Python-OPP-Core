from bank import Bank
from exceptions import *
from Logger_config import logger

def main():
    bank = Bank()

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose option: ")

        try:
            if choice == "1":
                acc_no = input("Account Number: ")
                name = input("Name: ")
                bank.create_account(acc_no, name)
                print("Account created successfully")

            elif choice == "2":
                acc_no = input("Account Number: ")
                amount = float(input("Amount: "))
                account = bank.get_account(acc_no)
                account.deposit(amount)
                print("Deposit successful")

            elif choice == "3":
                acc_no = input("Account Number: ")
                amount = float(input("Amount: "))
                account = bank.get_account(acc_no)
                account.withdraw(amount)
                print("Withdrawal successful")

            elif choice == "4":
                acc_no = input("Account Number: ")
                account = bank.get_account(acc_no)
                print("Balance:", account.get_balance())

            elif choice == "5":
                bank.save_data()
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")


        except Exception as e:
            print("Error:", e)
            logger.error(str(e))

if __name__ == "__main__":
    main()
