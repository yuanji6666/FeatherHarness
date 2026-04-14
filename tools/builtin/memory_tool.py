from langchain.tools import tool

from memory.save import save_memory

@tool("memory", description="a tool to save memory;" \
"When you feel that you need to remember certain preferences or information of users, save memory of type user\n" \
"when you make mistakes you need to remember user feedback, save memory of type feedback\n" \
"不要把name写得太宽泛，根据具体记忆关键词下划线隔开，最少4个词，在description参数应该是一次记忆的压缩在10-20词左右，type必须是user和feedback其中之一")
def memory(name: str, description:str, type: str, content: str) -> str:
	try:
		return save_memory(name=name, description=description, type=type, content=content)
	except Exception as exc:
		return (
			f"ERROR: {exc}. "
			"Please check whether the memory type is valid and try again with type='user' or type='feedback'."
		)

