# Ledger Core - double-entry engine
#type-aware balances: work in progress\

# BAD LINE - remove me

class InvalidEntryError(Exception):
    pass

class Account:
    def __init__(self, name, acct_type, balance = 0):
        self.name = name
        self.acc_type = acct_type
        self.balance = balance

class JournalEntry:
    def __init__(self, debit, credit, amount):
        self.debit = debit
        self.credit = credit
        self.amount = amount

class Ledger:
    def __init__(self):
        self.accounts = []
        self.entries = []
    
    def post(self, entry):
        if entry.amount <= 0:
            raise InvalidEntryError("Amount should be a positive number")
        entry.debit.balance += entry.amount
        entry.credit.balance -= entry.amount
        self.entries.append(entry)

    def add_account(self, account):
        self.accounts.append(account)

    def trial_balance(self):
        total = 0
        for account in self.accounts:
            total = total + account.balance
        return total