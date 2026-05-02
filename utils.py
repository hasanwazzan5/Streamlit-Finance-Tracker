#data access and helper functions
from db import Session, Transaction


def create_transaction(amount, category, transaction_type, transaction_date):
    session = Session()
    try:
        new_transaction = Transaction(
            amount=amount,
            category=category,
            type=transaction_type,
            date=str(transaction_date)
        )

        session.add(new_transaction)
        session.commit()

    finally:
        session.close()

def get_transactions():
    session = Session()
    try:
        transactions = session.query(Transaction).all()
        return transactions
    finally:
        session.close()

def get_transaction_by_id(id):
    session = Session()
    try:
        transaction = session.query(Transaction).filter(Transaction.id == id).first()
        return transaction
    finally:
        session.close()

def delete_transaction(transaction_to_delete):
    session = Session()
    try:
        session.delete(transaction_to_delete)
        session.commit()
    finally:
        session.close()


def calculate_totals(transactions):
    totals = {}

    for t in transactions:
        if t.category not in totals:
            totals[t.category] = 0

        if t.type == "Expense":
            totals[t.category] -= t.amount
        else:
            totals[t.category] += t.amount

    return totals