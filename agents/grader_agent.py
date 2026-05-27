# agents/grader_agent.py
from core.llm import get_llm_instance
from core.prompts import GRADE_PROMPT

def grade_answer_stream(question, student_answer):
    """
    主考官阅卷 Agent（百分制看板 + 亮点分析 + 致命错因 + 提分特训）
    """
    llm = get_llm_instance()
    final_prompt = GRADE_PROMPT.format(
        question=question, 
        student_answer=student_answer
    )
    
    # 流式返回批改报告
    for chunk in llm.stream(final_prompt):
        yield chunk.content