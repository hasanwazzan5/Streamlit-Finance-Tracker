#stream app front end
import streamlit as st
from datetime import date

import utils
from db import initialise_database

#init
initialise_database()

#title
st.title("💰 Personal Finance Tracker")

#inputs
col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("Amount", value=0.0)
    category = st.text_input("Category")

with col2:
    transaction_type = st.selectbox("Type", ["Expense","Income"])
    transaction_date = st.date_input("Date", value=date.today())

#button
if st.button("Add Transaction"):
    try:
        if category.strip() == "":
            st.error("Category cannot be empty")

        elif amount <= 0:
            st.error("Amount must be greater than 0")

        else:
            utils.create_transaction(
                amount=amount,
                category=category,
                transaction_type=transaction_type,
                transaction_date=transaction_date
            )

            st.success("Transaction Saved!")

    except Exception as e:
            st.error(f"Something went wrong: {e}")

#get transcation data
transactions = utils.get_transactions()

#search bar
search = st.text_input("Search category")
if search:
    transactions = [t for t in transactions if search.lower() in t.category.lower()]

#sorting
sort_option = st.selectbox("Sort by", ["Date", "Amount"])
if sort_option == "Amount":
    transactions.sort(key=lambda x: x.amount)
else:
    transactions.sort(key=lambda x: x.date)

#all transactions section
st.subheader("All Transactions")
st.table([
    {
        "ID": t.id,
        "Amount": t.amount,
        "Category": t.category,
        "Type": t.type,
        "Date": t.date
    }
    for t in transactions
])

#delete transaction
col3, col4 = st.columns(2)
with col3:
    st.subheader("Delete Transaction")
    delete_id = st.number_input("Enter Transaction ID to delete", step=1, min_value=1)

    if st.button("Delete"):
        try:
            transaction_to_delete = utils.get_transaction_by_id(delete_id)

            if transaction_to_delete:
                utils.delete_transaction(transaction_to_delete)
                st.success("Transaction deleted!")
            else:
                st.error("Transaction not found")

        except Exception as e:
            st.error(f"Error: {e}")

#totals section
with col4:
    st.subheader("Totals per Category")
    totals = utils.calculate_totals(transactions)
    st.table([
        { "Total": total, "Category": category }
        for category, total in totals.items() 
    ])