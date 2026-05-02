# 💰 Personal Finance Tracker (Streamlit)

A simple personal finance tracking web app built with Python and Streamlit.  
Users can add, view, filter, sort, and delete financial transactions, and analyze income vs expenses.

---

## 📌 Features

### Core Features
- Add income and expense transactions
- Categorize transactions
- Track transaction date
- Delete transactions by ID
- View all stored transactions

### Data Tools
- Search transactions by category
- Sort by date or amount
- Input validation (prevents empty categories and invalid values)
- Error handling for safe database operations

---

## 🧱 Tech Stack
- Python
- Streamlit
- SQLAlchemy
- SQLite

---

## 📁 Project Structure
project/
│
├── app.py # Streamlit UI (main app)
├── db.py # Database connection setup
├── models.py # Database schema (Transaction model)
├── utils.py # Helper functions (e.g. totals calculation)
├── finance.db # SQLite database file (auto-generated)
├── requirements.txt
└── README.md

---

## 🗄️ Database Schema

### Transaction Table
| Field    | Type    | Description              |
|----------|--------|--------------------------|
| id       | Integer | Primary key              |
| amount   | Float   | Transaction amount       |
| category | String  | Category (e.g. food)     |
| type     | String  | income or expense        |
| date     | String  | Transaction date         |

---

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd project

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
streamlit run app.py