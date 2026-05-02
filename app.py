#stream app front end
import streamlit as st
import matplotlib.pyplot as plt
from datetime import date

import utils
import ai
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

#all transactions section
st.divider()
st.subheader("All Transactions")

col1, col2 = st.columns(2)
#search bar
with col1:
    search = st.text_input("Search category")
    if search:
        transactions = [t for t in transactions if search.lower() in t.category.lower()]

#sorting
with col2:
    sort_option = st.selectbox("Sort by", ["Date", "Amount"])
    if sort_option == "Amount":
        transactions.sort(key=lambda x: x.amount)
    else:
        transactions.sort(key=lambda x: x.date)

st.table([
    {
        "ID": t.id,
        "Amount": f"{t.amount:.3f}",
        "Category": t.category,
        "Type": t.type,
        "Date": t.date
    }
    for t in transactions
])

#delete transaction
col1, col2 = st.columns(2)
with col1:
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
with col2:
    st.subheader("Totals per Category")
    totals = utils.calculate_totals(transactions)
    st.table([
        { "Total": f"{total:.3f}", "Category": category }
        for category, total in totals.items() 
    ])

#data analytics (data science bonus)
st.divider()
col1, col2 = st.columns(2)
income, expense, balance = utils.calculate_summary(transactions)

with col1:
    st.subheader("Financial Summary")
    st.metric("Income", f"{income:.3f}")
    st.metric("Expense", f"{expense:.3f}")
    st.metric("Balance", f"{balance:.3f}")

with col2:
    st.subheader("Income vs Expense")
    if income > 0 or expense > 0:
        fig, ax = plt.subplots()
        ax.pie(
            [income, expense],
            labels=["Income", "Expense"],
            autopct="%1.1f%%"
        )
        st.pyplot(fig)
    else:
        st.info("No transaction data yet.")

#ai feature
st.divider()
st.subheader("AI Insights")

if st.button("Generate AI Insights"):
    with st.spinner("Generating insights..."):
        insight = ai.generate_ai_insights()

    st.write(insight)