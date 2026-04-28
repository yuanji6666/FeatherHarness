from langchain.agents.middleware import SummarizationMiddleware

from model.factory import create_chat_model

def get_summarization_middleware():
    return SummarizationMiddleware(
        model=create_chat_model(),
        trigger=[
            ("messages", 20),
            ("tokens", 50000),
            ("fraction", 0.5)
        ],
        keep=('messages', 10)
)