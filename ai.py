#get ai recommendations
import os
import requests
import utils
import streamlit as st

def generate_ai_insights():
    transactions = utils.get_transactions()

    database_string = "\n".join(
    f"{t.id}, {t.amount}, {t.category}, {t.type}, {t.date}"
    for t in transactions
    )

    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload, timeout=20)
        return response.json()

    try:
        response = query({
            "messages": [
                {
                    "role": "user",
                    "content": 
                        f"Give an 1 sentence insight/ recommendation to a user based on this financial data {database_string}"
                }
            ],
            "model": "openai/gpt-oss-120b:cerebras"
        })
        return response['choices'][0]['message']['content']

    except:
            return "AI insight unavailable."
            