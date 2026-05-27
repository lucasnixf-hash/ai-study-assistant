# agents/tutor_agent.py
from rag.vector_store import get_vectorstore
from core.llm import get_llm_instance
from core.prompts import TUTOR_PROMPT

def tutor_stream_chat(question, history_messages):
    """
    苏格拉底式启发教学 Agent（支持流式输出 + 多轮记忆 + RAG 教材锁定）
    """
    db = get_vectorstore()
    docs = []
    
    # RAG 检索安全熔断机制：当知识库为空时，平滑切换到通识导师模式
    try:
        if db._collection.count() > 0:
            # 检索与学生问题最相关的 3 个文本块
            docs = db.as_retriever(search_kwargs={"k": 3}).invoke(question)
    except Exception as e:
        print(f"⚠️ 向量库检索异常（可能库未初始化）: {e}")
    
    # 解析上下文与教材出处
    context = "\n\n".join([d.page_content for d in docs]) if docs else "（未检索到特定的本地教材，请开启通识教学模式）"
    sources = set([d.metadata.get("source", "未知文献") for d in docs]) if docs else []

    # 格式化多轮对话历史历史（限制最近6条，防止撑爆小模型上下文）
    formatted_history = ""
    for msg in history_messages[-6:]:
        role = "学生" if msg["role"] == "user" else "教授"
        formatted_history += f"{role}: {msg['content']}\n"

    # 填充强化 Prompt 模板
    final_prompt = TUTOR_PROMPT.format(
        context=context, 
        chat_history=formatted_history, 
        question=question
    )
    
    # 动态调配底层 LLM 引擎（本地或云端）并实现流式吐出
    llm = get_llm_instance()
    for chunk in llm.stream(final_prompt):
        yield chunk.content

    # 如果有本地教材参考，在流的最后优雅附带出来
    if sources:
        yield f"\n\n---\n📚 *基于专属教材线索：{', '.join(sources)}*"