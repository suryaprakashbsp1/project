class Account:
    def __init__(self, account_id, name, initial_balance=0):
        """Initialize account attributes."""
        self.account_id = account_id
        self.name = name
        self.balance = initial_balance
        self.payees = []
        self.transaction_history = []

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")

    def add_payee(self, payee_account_id):
        """Add a payee to the account."""
        if payee_account_id not in self.payees:
            self.payees.append(payee_account_id)
            print(f"Payee {payee_account_id} added successfully.")
        else:
            print("Payee already exists.")

    def transfer(self, payee_account_id, amount, accounts):
        """Transfer money to a payee."""
        if payee_account_id not in self.payees:
            print("Payee not found.")
            return

        if payee_account_id not in accounts:
            print("Target account does not exist.")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        # Transfer money
        self.balance -= amount
        accounts[payee_account_id].balance += amount

        # Save transaction history
        self.transaction_history.append(
            f"Transferred ₹{amount} to {payee_account_id}"
        )

        accounts[payee_account_id].transaction_history.append(
            f"Received ₹{amount} from {self.account_id}"
        )

        print(f"₹{amount} transferred successfully to {payee_account_id}.")

    def view_transaction_history(self):
        """Display the account's transaction history."""
        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions found.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

    def view_details(self):
        """Display the account's details."""
        print("\nAccount Details")
        print("----------------------")
        print(f"Account ID : {self.account_id}")
        print(f"Name       : {self.name}")
        print(f"Balance    : ₹{self.balance}")
        print(f"Payees     : {self.payees}")


def main():
    """Main program for the Virtual Banking Application."""

    # Create accounts
    acc1 = Account("A101", "Surya", 1000)
    acc2 = Account("A102", "Rahul", 500)

    # Store accounts in dictionary
    accounts = {
        "A101": acc1,
        "A102": acc2
    }

    # Banking operations
    acc1.deposit(500)
    acc1.withdraw(200)

    acc1.add_payee("A102")
    acc1.transfer("A102", 300, accounts)

    # View account details
    acc1.view_details()
    acc2.view_details()

    # View transaction history
    acc1.view_transaction_history()
    acc2.view_transaction_history()


if __name__ == "__main__":
    main()