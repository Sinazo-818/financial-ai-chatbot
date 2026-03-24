from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI

def load_data():
    with open("financial data.txt", "r") as f:
        return f.read()

financial_context = load_data()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


st.title("📊 Financial AI Chatbot")

st.write("Ask questions about financial data (Apple, Microsoft, Tesla)")

user_input = st.text_input("Enter your question:")

def ask_llm(question):
    try:
        prompt = f"""
        You are a financial analyst.

        Use ONLY the data below to answer.

        If the question is about the future, say:
       "I do not have enough information to answe future-oriented questions."

        DATA
        {financial_context}

        QUESTION
        {question}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception:
        return "⚠️ API issue or limit reached. Please try again later."

if user_input:
    if st.button("Ask"):
        answer = ask_llm(user_input)
        st.success(answer)


load_dotenv()
