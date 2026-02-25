from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.orchestrator import ask

app = FastAPI(
    title="AI SQL Chat Assistant",
    description="Natural language to SQL chatbot",
    version="1.0.0",
)

# Allow frontend (Next.js) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Request / Response Models
# -------------------------

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    sql: str | None = None
    data: list | None = None

# -------------------------
# API Route
# -------------------------

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """
    Thin HTTP layer over existing orchestrator.ask()
    """
    result = ask(req.message)

    # Ensure result is serializable
    return {
        "answer": result.get("answer"),
        "sql": result.get("sql"),
        "data": result.get("data"),
    }
