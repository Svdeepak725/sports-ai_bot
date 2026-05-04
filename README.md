# sports-ai_bot
An AI-powered Sports Chatbot Dashboard that provides instant answers about players, matches, statistics, and tournaments.
Built using LangChain, LangGraph, and LangSmith, this project demonstrates how to create structured, scalable, and reliable LLM applications.

 Features
 AI chatbot for sports-related queries
 Multi-model support with fallback mechanism
 Structured workflows using LangGraph
 Debugging and tracing with LangSmith
 Interactive dashboard built with Streamlit
 Clean and responsive UI

Tech Stack
Language: Python
Frameworks: LangChain, LangGraph, LangSmith
Frontend/UI: Streamlit
Models: OpenAI / Gemini / Graq
Tools: Postman (API testing), Git

# Clone repository
git clone https://github.com/your-username/sports-ai-bot.git

# Move into project folder
cd sports-ai-bot

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
