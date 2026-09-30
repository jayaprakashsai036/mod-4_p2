from fastapi import APIRouter
from ..models.chat import ChatRequest, ChatResponse, HealthResponse
from ..services.agent import Agent

router = APIRouter()
agent = Agent()

@router.get("/health", response_model=HealthResponse)
def health():
    return {"status": "ok"}

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply, context = agent.run(request.user_id, request.message)
    return {"reply": reply, "context_used": context}
