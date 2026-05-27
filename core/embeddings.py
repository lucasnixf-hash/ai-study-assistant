from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings
import streamlit as st
from config.settings import DEFAULT_EMBEDDING_MODEL

class LocalEmbedding(Embeddings):
    def __init__(self):
        self.model = get_embedding_model_cache()

    def embed_documents(self, texts):
        cleaned = [str(t).replace("\x00", " ").strip() for t in texts if t is not None]
        cleaned = [s for s in cleaned if len(s) > 0]
        if not cleaned: return []
        return self.model.encode(cleaned, normalize_embeddings=True).tolist()

    def embed_query(self, text):
        s = str(text).replace("\x00", " ").strip()
        return self.model.encode([s], normalize_embeddings=True)[0].tolist()

@st.cache_resource
def get_embedding_model_cache():
    # 产品化优化：针对无 GPU 的普通用户设备，强制使用 CPU 确保 100% 稳定运行
    return SentenceTransformer(DEFAULT_EMBEDDING_MODEL, device="cpu")