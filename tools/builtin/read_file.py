from langchain.tools import tool


@tool
def read_file(file_path: str, limit: int = 0, offset: int = 0):
    """ read_file tool
    读取文件内容
    
    Args:
        file_path: 文件路径
        limit: 读取行数限制，0表示不限制
        offset: 起始行偏移量，默认从0开始
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if offset > 0:
        lines = lines[offset:]
    
    if limit > 0:
        lines = lines[:limit]
    
    return ''.join(lines)


if __name__ == '__main__':
    print(read_file.invoke("test.txt"))