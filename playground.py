#this file has no relation with whis project
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

reasoning_config = {
    "effort": "high",  # 推理强度：low / medium / high / none（禁用）
    "summary": "detailed"  # 推理摘要：auto / detailed / None（不返回）
}

model = ChatOpenAI(
    base_url="http://10.21.198.60:1234/v1",
    model="qwen/qwen3.5-9b",
    streaming=True,
    use_responses_api=True,
    reasoning=reasoning_config
)


