from langchain.tools import tool


@tool
def edit_file(file_path: str, old_string: str, new_string: str, replace_all: bool = False):
    """ edit_file tool
    编辑文件内容，精确匹配old_string并替换为new_string
    
    Args:
        file_path: 文件路径
        old_string: 需要替换的旧字符串，必须精确匹配
        new_string: 替换后的新字符串
        replace_all: 是否替换所有匹配项，默认False只替换第一个
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if replace_all:
        new_content = content.replace(old_string, new_string)
    else:
        if old_string not in content:
            return f"Error: old_string not found in file"
        new_content = content.replace(old_string, new_string, 1)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return "File updated successfully"


if __name__ == '__main__':
    print(edit_file.invoke("test.txt", old_string="hello", new_string="world"))