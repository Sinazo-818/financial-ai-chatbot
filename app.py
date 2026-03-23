from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets("OPENAI_API_KEY"))


st.title("📊 Financial AI Chatbot")

st.write("Ask questions about financial data (Apple, Microsoft, Tesla)")

user_input = st.text_input("Enter your question:")


def ask_llm(question):
    prompt = f"""
    You are a financial analyst.

    Only use the provided data.
    Do NOT make predictions.

    Question: {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


if st.button("Ask"):
    if user_input:
        answer = ask_llm(user_input)
        st.write("### Answer:")
        st.write(answer)


load_dotenv()
