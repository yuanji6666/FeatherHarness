from langchain.tools import tool


@tool
def write_file(file_path: str, content: str):
    """ write_file tool
    写入文件内容，新建文件或覆盖已有文件
    
    Args:
        file_path: 文件路径
        content: 要写入的内容
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return "File written successfully"


if __name__ == '__main__':
    print(write_file.invoke("test.txt", content="hello world"))