from langchain.tools import tool
import memory


@tool("recall", description="这个工具可以让你回想一段记忆的具体内容，name参数必须是记忆的名字，不要写其他的")
def recall(name: str):
    try:
        return memory.recall(name)
    except ValueError:
        return f"error: {ValueError}"