from .type import get_memory_root


def load_memory():
    memory = """# 过往记忆

下面是你之前想要记住的记忆，包含用户信息，偏好，错误反馈，如果你要查看具体消息，请调用recall工具：（记忆格式: [type]name - description ）
    """
    
    memory_root = get_memory_root()
    if memory_root is None:
        raise ValueError("MEMORY_PATH doesnt exist")

    memory_root.mkdir(parents=True, exist_ok=True)
    memory_file = memory_root / "MEMORY.md"
    
    if not memory_file.exists():
        memory_file.touch()
        return memory + "当前还没有记忆"
    
    return memory + memory_file.read_text()
