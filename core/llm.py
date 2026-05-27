from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import streamlit as st

def get_llm_instance():
    """
    根据 UI 中的动态配置，返回对应的 LLM 实例（单例缓存思想）
    """
    provider = st.session_state.get("llm_provider", "本地 Ollama")
    
    if provider == "本地 Ollama":
        model_name = st.session_state.get("ollama_model", "qwen2.5:1.5b")
        return ChatOllama(model=model_name, temperature=0.1, num_ctx=4096)
    
    else:
        # 在线云端 API 模式 (兼容 DeepSeek / OpenAI / 阿里云千问)
        api_key = st.session_state.get("api_key", "")
        base_url = st.session_state.get("api_base_url", "https://api.deepseek.com/v1")
        model_name = st.session_state.get("cloud_model", "deepseek-chat")
        
        if not api_key:
            # 防呆设计：如果用户没填 Key，优雅降级提示，不让程序崩溃
            raise ValueError("⚠️ 检测到您选择了云端 API 模式，但尚未填写 API Key，请在侧边栏配置后再使用。")
            
        return ChatOpenAI(
            model_name=model_name,
            openai_api_key=api_key,
            openai_api_base=base_url,
            temperature=0.1
        )