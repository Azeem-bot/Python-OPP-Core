import json
from account import Account
from exceptions import AccountNotFoundError
from Logger_config import logger


class Bank:

    def __init__(self):
        self.accounts = {}  # Dictionary: account_number -> Account object
        self.load_data()

    def create_account(self, account_number, name):
        if account_number in self.accounts:
            raise Exception("Account already exists")

        account = Account(account_number, name)
        self.accounts[account_number] = account

        logger.info(f"Account created: {account_number}")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account not found")

        return self.accounts[account_number]

    def save_data(self):
        data = {
            acc_no: acc.to_dict()
            for acc_no, acc in self.accounts.items()
        }

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        logger.info("Data saved successfully")

    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

                for acc_no, acc_data in data.items():
                    account = Account(
                        acc_data["account_number"],
                        acc_data["name"],
                        acc_data["balance"]
                    )
                    self.accounts[acc_no] = account

                logger.info("Data loaded successfully")

        except FileNotFoundError:
            # First time running the program
            logger.warning("No existing data file found. Starting fresh.")
