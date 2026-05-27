# rag/splitter.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(docs):
    """
    针对教材、大纲进行高聚合切分。
    chunk_size 设为 550，chunk_overlap 设为 80，
    既保证了上下文信息完整度，又不会让 qwen2.5:1.5b 这类小模型因为上下文过长而反应迟钝。
    """
    if not docs:
        return []
        
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=550,
        chunk_overlap=80,
        separators=["\n\n", "\n", "。", "！", "？", " ", ""]
    )
    
    chunks = splitter.split_documents(docs)
    print(f"🧩 [Splitter] 成功将文档切分为 {len(chunks)} 个高聚合文本块")
    return chunks