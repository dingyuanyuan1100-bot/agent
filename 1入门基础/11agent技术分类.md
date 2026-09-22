Agent 大类									子类型											核心释义
Chatbots 普通对话机器人						Customer Support								客服机器人，航班、酒店预订这类业务对话
											Prompt Generation from User Requirements		根据用户需求自动生成提示词，搭建信息收集类对话机器人
											Code Assistant									代码助手，代码分析、代码生成
											Multi-Agent 									Systems


多智能体系统									Collaboration									协作模式：2 个 Agent 互相配合完成任务
											Supervision										监督模式：一个主控 LLM，负责给多个子 Agent 分配任务、协调调度
											Hierarchical Teams								分层团队：嵌套多层 Agent，类似公司上下级组织，解决复杂大任务


RAG 检索增强生成								Adaptive RAG 自适应 RAG							根据提问动态切换检索策略，处理模糊、复杂问题，拿到最相关资料
											Agentic RAG 智能体式 RAG							把检索交给 Agent 自主决策：自动改写查询词、多次调用检索工具，反复迭代获取准确信息
											Corrective RAG 纠错 RAG							增加反馈校验环节，评估并修正回答，抑制大模型幻觉，提升答案准确度
											Self-RAG 自检索 RAG								自带记忆能力，记住历史对话，保证多轮对话上下文连贯


Planning Agents 规划型智能体					Plan-and-Execute								经典「规划 + 执行」：Agent 先拆解任务做计划，再一步步执行计划（上一张 Jarvis Agent 就属于这类）
											Reasoning without Observation					将环境观察结果保存为变量，减少重复规划，节省算力
											LLMCompiler										LLM 编译器，把任务规划转化为 DAG 有向无环图，流式调度执行任务


Reflection & Critique反思与自检				Basic Reflection								基础反思：Agent 输出答案之后，自己回看、修改输出内容
											Reflexion										经典论文方案，找出回答缺失、冗余的地方，指导下一轮优化 
											Language Agent Tree Search语言智能体树搜索			结合反思 + 奖励机制，像搜索树一样尝试多条解决路径，选出最优方案


Evaluation 评估体系							Agent-based										用另一个智能体模拟真实用户，去测试、评估聊天机器人效果
											In LangSmith									在 LangSmith 平台，基于对话数据集做 Agent 应用评测（LangChain 配套评测工具）