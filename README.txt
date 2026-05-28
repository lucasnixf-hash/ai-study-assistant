========================================================================
             🧠 AI Study Assistant v4 - 产品版使用指南手册
             🧠 AI Study Assistant v4 - Product User Guide & Manual
========================================================================

【产品简介 / Introduction】
🇨🇳 本系统是一款基于 RAG (检索增强生成) 与多智能体架构 (Multi-Agent) 打造的个性化智能学习助手。系统专门针对“理解驱动型”和“偏图像化、感知记忆型”的学习风格进行了提示词强约束，采用苏格拉底式引导教学，绝不直接喂出答案，旨在帮助用户攻克复杂的算法、系统底层架构、离散数学等硬核高校课程。

🇬🇧 This system is a personalized intelligent study assistant built on RAG (Retrieval-Augmented Generation) and a Multi-Agent architecture. Tailored specifically for "understanding-driven" and "visual/perceptual memory" learning styles, the system strictly enforces prompt constraints to employ Socratic guided teaching. It never feeds direct answers, aiming to help users conquer hardcore college courses like complex algorithms, low-level system architectures, and discrete mathematics.

------------------------------------------------------------------------
一、 极简环境配置（首次使用） / I. Minimalist Environment Setup (First-time Use)
------------------------------------------------------------------------
1. 🇨🇳 确保本地已安装 Python 3.9+ 环境。
   🇬🇧 Ensure Python 3.9+ is installed locally.

2. 🇨🇳 打开系统终端（Terminal / PowerShell），进入本项目的根目录。
   🇬🇧 Open your system terminal (Terminal / PowerShell) and navigate to the root directory of this project.

3. 🇨🇳 执行以下命令一键安装产品运行所需的全部依赖核心组件库：
   🇬🇧 Execute the following command to one-click install all core dependency libraries required to run the product:
   > pip install streamlit langchain langchain-ollama langchain-openai sentence-transformers chromadb pypdf

------------------------------------------------------------------------
二、 如何开启并进入系统 / II. How to Launch and Access the System
------------------------------------------------------------------------
1. 🇨🇳 如果你想使用【本地免费全离线模式】：请确保你本地已启动了 Ollama 服务，且提前下载好了模型（如：`ollama run qwen2.5:1.5b`）。
   🇬🇧 If you want to use the [Local Free Fully Offline Mode]: Ensure your local Ollama service is running and the model is downloaded in advance (e.g., `ollama run qwen2.5:1.5b`).

2. 🇨🇳 如果你想使用【云端极速模式】：无需在本地配置任何大模型，直接进入第3步，在界面中填写你的云端 API Key（如 DeepSeek）。
   🇬🇧 If you want to use the [Cloud High-Speed Mode]: No local LLM configuration is needed. Skip to step 3 and enter your cloud API Key (e.g., DeepSeek) directly in the UI.

3. 🇨🇳 一键启动命令：在系统终端的项目根目录下，键入并执行：
   🇬🇧 One-click Launch Command: In your terminal at the project root, type and execute:
   > streamlit run main_ui.py

4. 🇨🇳 运行成功后，系统会自动在你的浏览器中打开可视化交互看板：`http://localhost:8501`
   🇬🇧 Upon successful launch, the system will automatically open the visual interactive dashboard in your browser: `http://localhost:8501`

------------------------------------------------------------------------
三、 核心产品功能操作指南 / III. Core Product Features & Operations Guide
------------------------------------------------------------------------
1. 📚 【专属知识库云盘】（💥 强烈建议第一步使用） / [Exclusive Knowledge Base Cloud Drive] (💥 Highly recommended as your first step):
   🇨🇳 功能：告别枯燥的后台代码，直接将你的 PDF、TXT 格式的教材大纲或课程讲义拖拽上传，点击“注入”，AI 即可瞬间学习并锁定这些教材作为背景参考资料。
   🇬🇧 Feature: Say goodbye to tedious backend code. Directly drag and drop your PDF or TXT syllabus/lecture notes to upload. Click "Inject," and the AI will instantly learn and lock onto these materials as background reference context.

2. 💡 【启发式智能互动导师】 / [Heuristic Smart Interactive Tutor]:
   🇨🇳 功能：ChatGPT 式的多轮流式连贯对话。支持苏格拉底反问和生活化比喻讲解，支持点击“重置思维上下文”开启全新探讨。
   🇬🇧 Feature: ChatGPT-style multi-turn coherent streaming conversation. Supports Socratic questioning and relatable analogies for explanations. Includes a "Reset Context" button to start a fresh discussion.

3. 🎯 【考点自适应出题】 / [Adaptive Quiz Generation]:
   🇨🇳 功能：输入任意核心考点（如：二叉树遍历、0/1背包变体），一键生成集概念选择、逻辑判断、算法探究于一体的水平测试卷，并在末尾附带精准避坑解析。
   🇬🇧 Feature: Input any core topic (e.g., Binary Tree Traversal, 0/1 Knapsack variants), and one-click generate a proficiency test integrating conceptual multiple-choice, logical judgment, and algorithmic exploration, followed by precise pitfall-avoidance explanations.

4. 📝 【综合答卷深度批改】 / [In-depth Comprehensive Grading]:
   🇨🇳 功能：考前特训神器。左侧粘原题，右侧粘你的解答或代码，阅卷委员会将从综合得分、闪光点、致命错因诊断、提分特训建议四大维度为你输出详尽的批改看板。
   🇬🇧 Feature: The ultimate pre-exam training artifact. Paste the original question on the left and your answer/code on the right. The grading committee