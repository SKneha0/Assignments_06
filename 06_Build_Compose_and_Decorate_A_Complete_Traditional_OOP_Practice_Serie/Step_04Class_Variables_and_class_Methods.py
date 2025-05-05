class Bank:
    bank_name = "ABC Bank"  # class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Creating objects
acc1 = Bank("Ali")
acc2 = Bank("Neha")

# Showing default bank name
acc1.show_details()
acc2.show_details()

# Changing bank name using class method
Bank.change_bank_name("XYZ Bank")

# Showing updated bank name
acc1.show_details()
acc2.show_details()
