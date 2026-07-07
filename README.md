# Ledger Core

A double-entry accounting engine in Python — the bookkeeping model real accounting systems are built on.

## Why double-entry?
Every transaction moves an equal amount between two accounts: one debited, one credited.
Because debits and credits always match, the **trial balance always sums to zero** — and if it
ever doesn't, you know something is wrong. That built-in check is what makes double-entry
trustworthy, and it's the core guarantee this engine enforces.

## Features
- **Double-entry posting** — each journal entry debits one account and credits another by the same amount.
- **Trial balance** — sums every account balance; returns 0 for a valid set of books.
- **Input validation** — rejects non-positive amounts up front with a custom `InvalidEntryError`, so bad data never enters the ledger.
- **Readable objects** — accounts print clearly, e.g. `Account('Cash', balance=0)`.
- **Tested** — 10 passing `pytest` tests covering posting, balancing, and validation.

## Install
```bash
git clone https://github.com/rohithkrishnaer/ledger-core.git
cd ledger-core
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -e .
```

## Usage
```python
from ledger import Account, JournalEntry, Ledger

cash = Account("Cash", "asset")
sales = Account("Sales", "income")

ledger = Ledger()
ledger.add_account(cash)
ledger.add_account(sales)

ledger.post(JournalEntry(cash, sales, 100))   # debit Cash, credit Sales
print(cash)                 # Account('Cash', balance=100)
print(ledger.trial_balance())   # 0
```

## Tests
```bash
python -m pytest
```