# File: chat_chain.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Load Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini chat model instance
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=gemini_api_key
)

# Function to query Gemini with prompt
def get_gemini_response(prompt: str) -> str:
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
