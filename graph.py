from langgraph.graph import StateGraph
from router import route_model
from models import openai_llm, gemini_llm, groq_llm_response

def router_node(state):
    question = state["question"]
    return {"question": question, "model": route_model(question)}

def gemini_node(state):
    try:
        answer = gemini_llm(state["question"])
        if not answer:
            raise Exception("Empty response")
        return {"answer": answer}
    except:
        return {"answer": openai_llm.invoke(state["question"]).content}

def groq_node(state):
    try:
        answer = groq_llm_response(state["question"])
        if not answer:
            raise Exception("Empty response")
        return {"answer": answer}
    except:
        return {"answer": openai_llm.invoke(state["question"]).content}

def openai_node(state):
    return {"answer": openai_llm.invoke(state["question"]).content}

builder = StateGraph(dict)

builder.add_node("router", router_node)
builder.add_node("gemini", gemini_node)
builder.add_node("groq", groq_node)
builder.add_node("openai", openai_node)

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    lambda state: state["model"],
    {
        "gemini": "gemini",
        "groq": "groq"
    }
)

graph = builder.compile()