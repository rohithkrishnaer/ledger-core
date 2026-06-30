import pytest
from ledger import Account, JournalEntry, Ledger, InvalidEntryError

def test_trial_balance_is_zero():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    ledger.post(JournalEntry(cash, rent, 100))
    ledger.add_account(cash)
    ledger.add_account(rent)
    assert ledger.trial_balance() == 0

def test_negetive_amount_raises():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    with pytest.raises(InvalidEntryError):
        ledger.post(JournalEntry(rent, cash, -50))

def test_debit_account_balance():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    ledger.post(JournalEntry(cash, rent, 100))
    assert cash.balance == 100

def test_credit_account_balance():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    ledger.post(JournalEntry(rent, cash, 100))
    assert cash.balance == -100

def test_zero_amount():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    with pytest.raises(InvalidEntryError):
        ledger.post(JournalEntry(rent, cash, 0))

def test_add_account_grow_list():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    ledger.add_account(cash)
    ledger.add_account(rent)
    assert len(ledger.accounts) == 2

def test_new_account_starts_at_zero():
    cash = Account("cash", "asset")
    assert cash.balance == 0

def test_account_stores_name():
    cash = Account("cash", "asset")
    assert cash.name == "cash"

def test_post_records_entry():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    ledger.post(JournalEntry(cash, rent, 100))
    assert len(ledger.entries) == 1

def test_two_posts_accumulate():
    ledger = Ledger()
    cash = Account("cash", "asset")
    rent = Account("Rent", "Expense")
    ledger.post(JournalEntry(rent, cash, 100))
    ledger.post(JournalEntry(rent,cash, 100))
    assert rent.balance == 200