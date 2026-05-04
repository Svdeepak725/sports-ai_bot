def route_model(question):
    q = question.lower()

    if "why" in q or "explain" in q:
        return "groq"
    elif "who" in q or "stats" in q:
        return "gemini"
    else:
        return "gemini"