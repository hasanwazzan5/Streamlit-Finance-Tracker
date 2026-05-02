# 💰 Personal Finance Tracker (Streamlit + AI)

A simple personal finance tracking web app built with Python and Streamlit.  
The app allows users to manage transactions, analyze spending, and generate AI-powered financial insights.

---

## 🚀 Live Demo
(https://app-finance-tracker-ukmkgchmilstdbkwtvsguk.streamlit.app/)

---

## 📌 Features

### 🧾 Core Features
- Add income and expense transactions
- Categorise transactions
- Track transaction date
- Delete transactions
- Input validation and error handling

---

### 🔍 Data Controls
- Search transactions by category
- Sort by date or amount
- View full transaction history

---

### 📊 Analytics Dashboard (Data Science Bonus)
- Income vs expense summary
- Financial balance calculation
- Data visualization using charts

---

### 🤖 AI Feature (AI Bonus)
- AI-generated financial insights
- Provides personalized recommendations
- Uses a real model API (cloud-based)

---

## 🧱 Tech Stack
- Python
- Streamlit
- SQLAlchemy
- SQLite
- AI API

---

## 📁 Project Structure

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