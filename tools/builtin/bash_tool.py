import subprocess
import os
import re
from langchain.tools import tool

# 危险命令模式
DANGEROUS_PATTERNS = [
    r'rm\s+-rf\s+/',           # 删除根目录
    r'rm\s+-rf\s+\.',          # 删除当前目录
    r'dd\s+if=',               # 磁盘写入
    r'mkfs\.',                 # 格式化
    r':\(\)\{',                # fork bomb
    r'curl.*\|\s*sh',          # 远程脚本执行
    r'wget.*\|\s*sh',          # 远程脚本执行
    r'chmod\s+-R\s+777',       # 过度开放权限
    r'chown\s+-R',             # 改变所有者
    r'>\s*/dev/sd',            # 直接写入磁盘
    r'sudo\s+rm',              # sudo删除
    r'git\s+reset\s+--hard',   # git强制重置
    r'git\s+checkout\s+\.',    # git checkout覆盖
    r'git\s+restore\s+\.',     # git restore覆盖
    r'--no-verify',            # 跳过git hooks
    r'--no-gpg-sign',          # 跳过gpg签名
    r'git\s+push\s+--force',   # 强制push
    r'git\s+push\s+-f',        # 强制push
]

# 允许的命令白名单（可选）
ALLOWED_COMMANDS = [
    'ls', 'cat', 'pwd', 'echo', 'cd', 'mkdir', 'touch', 'cp', 'mv', 'grep', 'find',
    'head', 'tail', 'wc', 'sort', 'uniq', 'diff', 'git status', 'git diff',
    'git log', 'git branch', 'git show', 'git fetch', 'git pull',
]


def is_dangerous_command(command: str) -> bool:
    """检查命令是否危险"""
    cmd_lower = command.lower().strip()
    
    # 检查危险模式
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, cmd_lower):
            return True
    
    # 检查是否在白名单中
    for allowed in ALLOWED_COMMANDS:
        if cmd_lower.startswith(allowed) or cmd_lower == allowed:
            return False
    
    # 包含敏感操作的命令
    sensitive_patterns = [
        r'rm\s+-',              # rm带参数
        r'chmod\s+',            # chmod
        r'chown\s+',            # chown
        r'mkdir\s+-p',          # 创建目录
    ]
    
    for pattern in sensitive_patterns:
        if re.search(pattern, cmd_lower):
            return True
    
    return False


@tool
def run_bash(command: str):
    """ bash tool
    执行一条bash命令
    
    注意：以下命令被拦截：
    - 删除根目录或当前目录 (rm -rf /, rm -rf .)
    - 磁盘操作 (dd, mkfs)
    - 远程脚本执行 (curl | sh, wget | sh)
    - git危险操作 (reset --hard, checkout ., --no-verify)
    - 强制push (git push --force)
    """
    if is_dangerous_command(command):
        return f"Error: Dangerous command blocked: {command}"
    
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
    print(run_bash.invoke("ls ~"))
    print(run_bash.invoke("rm -rf /"))