# rag/loader.py
from langchain_core.documents import Document
import pypdf
import io

def load_uploaded_file(uploaded_file):
    """
    产品化核心：直接从 Streamlit 内存文件流中读取数据，不再需要落盘，速度极快
    支持上传多个文件，动态解析
    """
    docs = []
    file_name = uploaded_file.name
    
    if file_name.endswith(".pdf"):
        try:
            # 使用 pypdf 从 BytesIO 内存流中读取
            pdf_reader = pypdf.PdfReader(io.BytesIO(uploaded_file.read()))
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                if text:
                    # 将每页封装为 LangChain 的 Document 对象
                    docs.append(
                        Document(
                            page_content=text, 
                            metadata={"source": file_name, "page": page_num + 1}
                        )
                    )
        except Exception as e:
            print(f"❌ 解析 PDF 内存流失败 {file_name}: {str(e)}")
                
    elif file_name.endswith(".txt"):
        try:
            text = uploaded_file.read().decode("utf-8", errors="ignore")
            docs.append(
                Document(
                    page_content=text, 
                    metadata={"source": file_name}
                )
            )
        except Exception as e:
            print(f"❌ 解析 TXT 内存流失败 {file_name}: {str(e)}")
        
    return docs