<p align="center"><img src="ui/public/favicon.ico" alt="AIsisstant" width="120" /></p>
<h3 align="center">AIsisstant：开源智能程序设计助手</h3>
<p align="center">
  <a href="https://github.com/Yuelinfeng/AIsisstant">项目主页</a>
</p>
<hr/>

AIsisstant 是由 <b>Yuelinfeng</b>（2021214376@stu.cqupt.edu.cn）独立设计与开发的开源智能程序设计助手。

本项目集成了RAG（检索增强生成）、多模型编排与智能Agent协作，致力于为开发者和团队提供高效的程序设计辅助。

<b>主要贡献：</b>
- <b>知识库构建与高效检索：</b> 采用正则表达式和Python字符串处理技术实现文本分块，结合LangChain与多种主流Embedding模型（API/本地推理）进行向量化处理。通过Django ORM优化批量处理流程，显著提升知识库的构建效率和检索准确性。
- <b>多模型集成与灵活调用：</b> 基于LangChain及其插件体系，设计并实现抽象基类和工厂模式，有效支持多模型的灵活切换与统一调用，增强系统扩展性。
- <b>智能对话与Agent协作：</b> 运用LangChain框架实现多智能体协作机制。通过Django REST API和Celery异步任务，实现了复杂的对话流转、任务智能分解及工具自动化调用，提升用户交互体验与系统智能化水平。

## 快速开始

运行以下命令即可通过Docker启动AIsisstant：

```bash
docker run -d --name=aisisstant --restart=always -p 8080:8080 -v ~/.aisisstant:/var/lib/postgresql/data -v ~/.python-packages:/opt/aisisstant/app/sandbox/python-packages yuelinfeng/aisisstant
```

通过浏览器访问 `http://your_server_ip:8080`，默认管理员账号：
- 用户名：admin
- 密码：AIsisstant@123..

## 截图展示

<!-- 请替换为你自己的界面截图 -->

## 技术栈

- 前端：Vue3 + TypeScript + Element Plus
- 后端：Python 3.11, Django 4.2, Django REST Framework, Celery, LangChain
- 数据库：PostgreSQL + pgvector

## 项目亮点

- 所有核心模块（知识库、模型集成、API等）均由 <b>Yuelinfeng</b> 独立设计与实现。
- 非MaxKB或任何其他项目的fork。
- 注重代码质量、可扩展性与真实编程场景。

## License

本项目采用GPLv3协议。  
版权所有 (c) 2024 Yuelinfeng。

联系方式：2021214376@stu.cqupt.edu.cn

---

欢迎star和交流，如需合作或有任何建议，欢迎联系！
