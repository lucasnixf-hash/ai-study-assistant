import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 向量库本地持久化路径
CHROMA_PATH = os.path.join(BASE_DIR, "knowledge_base/chroma_db")

# 默认本地模型配置（用户可在 UI 中覆盖）
DEFAULT_EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
DEFAULT_LLM_MODEL = "qwen2.5:1.5b"