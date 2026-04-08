from langchain.tools import tool

@tool
def get_user_info() -> str:
    """这个工具可以用来获得用户的个人信息
    """
    return "我叫小源，今年19岁，在武汉大学大学计算机学院读大二"
