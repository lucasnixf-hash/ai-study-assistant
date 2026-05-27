import sys
import os
import streamlit as st

# 终极路径防线：确保在任何运行环境下根目录永远在最前
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from services.study_service import route_stream
from rag.loader import load_uploaded_file
from rag.splitter import split_documents
from rag.vector_store import save_to_chroma, clear_vector_db, get_vectorstore

st.set_page_config(page_title="AI Study Assistant v4", page_icon="🚀", layout="wide")

# ==================== 🛠️ 侧边栏：多端产品模型调配中心 ====================
with st.sidebar:
    st.title("⚙️ 引擎智能配置中心")
    st.markdown("---")
    
    provider = st.selectbox("🔮 模型底层驱动", ["本地 Ollama", "云端 API 模式"])
    st.session_state["llm_provider"] = provider
    
    if provider == "本地 Ollama":
        ollama_model = st.text_input("🤖 Ollama 模型名称", value="qwen2.5:1.5b")
        st.session_state["ollama_model"] = ollama_model
    else:
        st.warning("💡 支持 DeepSeek、千问、OpenAI 等标准接口")
        api_base_url = st.text_input("🔗 API Base URL", value="https://api.deepseek.com/v1")
        api_key = st.text_input("🔑 API Secret Key", type="password", placeholder="sk-...")
        cloud_model = st.text_input("🏷️ 云端模型代号", value="deepseek-chat")
        
        st.session_state["api_base_url"] = api_base_url
        st.session_state["api_key"] = api_key
        st.session_state["cloud_model"] = cloud_model

    st.markdown("---")
    st.caption("AI Study Assistant v4 Pro 产品版")

# ==================== 🏛️ 主界面：功能看板 ====================
st.title("🧠 AI Study Assistant v4")
st.caption("全自研个性化启发式学习控制台 —— 专为理解驱动与深度思考而生")

tabs = st.tabs(["📘 启发式智能互动导师", "📝 考点自适应出题", "💯 综合答卷深度批改", "📂 专属知识库云盘"])

# ----- TAB 1: 导师 -----
with tabs[0]:
    st.subheader("📘 启发式导师对话看板")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "你好！我是你的学术导师。拒绝死记硬背，让我们通过推导和比喻攻克每一个难点。请提问！"}]

    if st.button("🧹 重置思维上下文"):
        st.session_state.messages = [{"role": "assistant", "content": "历史记忆已清空，新的学术探讨开始！"}]
        st.rerun()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    if user_input := st.chat_input("输入你想探讨的概念或算法难题..."):
        with st.chat_message("user"): st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            res_placeholder = st.empty()
            full_res = ""
            try:
                payload = {"question": user_input, "history": st.session_state.messages[:-1]}
                for chunk in route_stream("tutor", payload):
                    full_res += chunk
                    res_placeholder.markdown(full_res + "▌")
                res_placeholder.markdown(full_res)
                st.session_state.messages.append({"role": "assistant", "content": full_res})
            except Exception as e:
                st.error(str(e))

# ----- TAB 2: 出题 -----
with tabs[1]:
    st.subheader("📝 考点自适应出题")
    topic = st.text_input("输入你想评测的知识点（如：CSAPP 异常控制流）：", key="topic_input")
    if st.button("🔥 生成全维评测卷", type="primary"):
        if topic:
            output = st.empty()
            txt = ""
            try:
                for chunk in route_stream("quiz", {"topic": topic}):
                    txt += chunk
                    output.markdown(txt + "▌")
                output.markdown(txt)
            except Exception as e: st.error(str(e))

# ----- TAB 3: 批改 -----
with tabs[2]:
    st.subheader("💯 综合答卷深度批改")
    col1, col2 = st.columns(2)
    with col1: q_text = st.text_area("📋 原题内容", height=150, placeholder="输入原题...", key="q_t")
    with col2: a_text = st.text_area("✍️ 你的解答/代码", height=150, placeholder="写下你的推导、小论文或代码实现...", key="a_t")
    
    if st.button("🚀 提请阅卷委员会批改", type="primary"):
        if q_text and a_text:
            output = st.empty()
            txt = ""
            try:
                for chunk in route_stream("grade", {"question": q_text, "student_answer": a_text}):
                    txt += chunk
                    output.markdown(txt + "▌")
                output.markdown(txt)
            except Exception as e: st.error(str(e))

# ----- TAB 4: 知识库（核心新增：UI级解耦管理） -----
with tabs[3]:
    st.subheader("📂 专属教材知识库管理面板")
    
    # 状态展示
    try:
        current_count = get_vectorstore()._collection.count()
    except Exception:
        current_count = 0
    st.metric("📊 当前知识库索引文本块数量", current_count)

    uploaded_files = st.file_uploader("📥 上传你的专业课教材/讲义/大纲 (支持 PDF、TXT)", accept_multiple_files=True, type=["pdf", "txt"])
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🚀 注入上传的教材到智能助手", type="primary"):
            if uploaded_files:
                all_chunks = []
                with st.spinner("正在进行高聚合文本切分..."):
                    for f in uploaded_files:
                        docs = load_uploaded_file(f)
                        chunks = split_documents(docs)
                        all_chunks.extend(chunks)
                
                with st.spinner("正在生成嵌入特征并建立索引..."):
                    added = save_to_chroma(all_chunks)
                    st.success(f"🎉 成功注入！知识库新增 {added} 条高聚合学术切片。")
                    st.rerun()
            else:
                st.warning("请先选择并上传文件。")
                
    with col_btn2:
        if st.button("🧹 一键粉碎/清空专属知识库", type="secondary"):
            clear_vector_db()
            st.success("💥 本地知识库已完全初始化清空。")
            st.rerun()