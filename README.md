 Project Overview

This project is a financial AI chatbot built using a Retrieval-Augmented Generation (RAG) approach.
The chatbot answers user questions based strictly on provided financial data, ensuring responses are controlled, explainable, and grounded in real information.

The application is deployed as an interactive web app using Streamlit, allowing users to query financial data in real time.

 Objective

To build a simple but practical AI system that:

Answers financial questions using structured company data
Avoids hallucination by restricting responses to known data
Demonstrates safe and explainable use of large language models
 Key Features
 Retrieval-Augmented Generation (RAG)
The chatbot uses local financial data as context
Responses are generated only from provided information
Prevents unsupported or speculative answers

 Controlled Prompt Design
Explicit instructions to:
Avoid predictions
Reject unknown queries
Ensures reliable and business-safe outputs
 Error Handling
Graceful handling of API limits and failures
User-friendly fallback messages
 Cloud Deployment
Deployed using Streamlit Community Cloud
API keys managed securely using environment secrets
 Data Source
The chatbot uses structured financial data for companies such as:
Apple
Microsoft
Tesla

Metrics include:
Revenue
Net Income
Cash Flow
Debt Ratio

 Tech Stack:
Python
Streamlit
OpenAI API
Prompt engineering (RAG approach)
Environment-based secret management

	How It Works:
User enters a financial question
The app loads structured financial data
The question + data are passed to the LLM
The model generates a response based only on the provided context
 Example Queries
“Compare Apple and Microsoft financially”
“Which company has the lowest debt ratio?”
“Which company generates the most cash flow?”
 
	Limitations:
Only answers questions based on the provided dataset
Cannot make predictions about future performance
API usage may be limited without billing enabled

	Key Skills Demonstrated:
LLM integration via API
Retrieval-Augmented Generation (RAG)
Prompt engineering
Streamlit app development
Cloud deployment
Error handling and reliability design
The answer is displayed in the web interface
