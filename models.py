import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import google.generativeai as genai

load_dotenv()

# 🔹 OpenAI (fallback)
openai_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 🔹 Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-pro")

# 🔹 Groq setup
groq_llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)

# 🔹 Gemini function
def gemini_llm(question):
    response = gemini_model.generate_content(question)
    return response.text

# 🔹 Groq function
def groq_llm_response(question):
    response = groq_llm.invoke(question)
    return response.content