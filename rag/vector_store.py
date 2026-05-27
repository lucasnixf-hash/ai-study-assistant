import os
import shutil
from langchain_community.vectorstores import Chroma
from core.embeddings import LocalEmbedding
from config.settings import CHROMA_PATH

def get_vectorstore():
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=LocalEmbedding())

def clear_vector_db():
    """产品化设计：允许用户一键清空旧的教材库"""
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    print("🧹 向量数据库已成功清空")

def save_to_chroma(chunks):
    if not chunks: return 0
    
    valid_chunks = []
    for c in chunks:
        content = getattr(c, "page_content", None)
        if content and isinstance(content, str) and content.strip():
            c.page_content = content.replace("\x00", " ").strip()
            valid_chunks.append(c)

    db = get_vectorstore()
    batch_size = 100
    for i in range(0, len(valid_chunks), batch_size):
        batch = valid_chunks[i:i + batch_size]
        db.add_documents(batch)
        
    return len(valid_chunks)