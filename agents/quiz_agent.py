# agents/quiz_agent.py
from core.llm import get_llm_instance
from core.prompts import QUIZ_PROMPT

def generate_quiz_stream(topic):
    """
    标准教务处命题 Agent（强指令约束输出四个板块，带精准解析）
    """
    llm = get_llm_instance()
    final_prompt = QUIZ_PROMPT.format(topic=topic)
    
    # 流式返回生成的试卷文本
    for chunk in llm.stream(final_prompt):
        yield chunk.content