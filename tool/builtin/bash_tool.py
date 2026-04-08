import subprocess
import os
from langchain.tools import tool

@tool
def run_bash(command: str):
    """ bash tool
    执行一条bash命令
    """
    result = subprocess.run(
            command,
            shell=True,
            cwd=os.getcwd(),
            capture_output=True,
            text=True,
            timeout=120,
        )
    return result.stdout

if __name__ == '__main__':
    print(run_bash.invoke("ls"))