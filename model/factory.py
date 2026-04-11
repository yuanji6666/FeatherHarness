from langchain_openai import ChatOpenAI
from langchain.chat_models import BaseChatModel
from langchain_core.rate_limiters import InMemoryRateLimiter
import os

def create_chat_model(
    model_name: str | None = None
) -> BaseChatModel:
    limiter = InMemoryRateLimiter(
        requests_per_second=0.1
    )

    return ChatOpenAI(
        base_url=os.getenv("OPENAI_BASE_URL") or "https://api.qnaigc.com/v1",
        model=model_name or os.getenv("OPENAI_MODEL_NAME") or "xiaomi/mimo-v2-flash",
        streaming=True,
        rate_limiter=limiter,
    )

