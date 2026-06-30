# Ledger Core

A double-entry bookkeeping engine in pure Python, with a pytest test suite.

Every transaction is recorded in two accounts — one debited, one credited, by equal
amounts — so the books always balance. The engine enforces that invariant and rejects
invalid entries.

## Concepts
- **Account** — a name, a type (asset/liability/equity/income/expense), and a balance.
- **JournalEntry** — one transaction: a debit account, a credit account, an amount.
- **Ledger** — holds accounts and entries; posts transactions and produces a trial balance.

## The double-entry rule
On every post, the debit account increases and the credit account decreases by the same
amount — so the **trial balance (sum of all balances) is always 0**. Non-positive amounts
are rejected with a custom `InvalidEntryError`.

## Usage
```python
ledger = Ledger()
cash = Account("Cash", "asset")
rent = Account("Rent Expense", "expense")
ledger.add_account(cash)
ledger.add_account(rent)

ledger.post(JournalEntry(rent, cash, 100))   # pay £100 rent

print(rent.balance)            # 100
print(cash.balance)            # -100
print(ledger.trial_balance())  # 0  ✓ balanced
```

## Tests
```bash
pip install pytest
pytest
```
10 tests cover posting, balance direction, the trial-balance invariant, validation, and accumulation.

## Built with
Pure Python + pytest. No external dependencies.