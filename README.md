<p align="center"><img src="ui/public/favicon.ico" alt="AIsisstant" width="120" /></p>
<h3 align="center">AIsisstant: An Open-Source AI Programming Assistant</h3>
<p align="center">
  <a href="https://github.com/Yuelinfeng/AIsisstant">Project Home</a>
</p>
<hr/>

AIsisstant is an open-source AI assistant for programming, independently designed and developed by <b>Yuelinfeng</b> (2021214376@stu.cqupt.edu.cn).

The project integrates Retrieval-Augmented Generation (RAG), multi-model orchestration, and intelligent agent collaboration, aiming to provide efficient programming assistance for developers and teams.

<b>Main Contributions:</b>
- <b>Knowledge Base Construction & Efficient Retrieval:</b> Implements advanced text chunking and vectorization using regex and Python string processing, supports multiple embedding models (API/local), and optimizes batch processing with Django ORM, significantly improving knowledge base construction efficiency and retrieval accuracy.
- <b>Multi-Model Integration & Flexible Invocation:</b> Based on LangChain and its plugin system, designed and implemented abstract base classes and factory patterns to support flexible switching and unified invocation of various LLMs, enhancing system extensibility.
- <b>Intelligent Dialogue & Agent Collaboration:</b> Utilizes LangChain to realize multi-agent collaboration. With Django REST API and Celery asynchronous tasks, supports complex dialogue flows, intelligent task decomposition, and tool automation, greatly improving user experience and system intelligence.

## Quick Start

Run the following command to start AIsisstant with Docker:

```bash
docker run -d --name=aisisstant --restart=always -p 8080:8080 -v ~/.aisisstant:/var/lib/postgresql/data -v ~/.python-packages:/opt/aisisstant/app/sandbox/python-packages yuelinfeng/aisisstant
```

Access the web interface at `http://your_server_ip:8080` with default admin credentials:
- username: admin
- password: AIsisstant@123..

## Screenshots

<!-- Please replace with your own screenshots -->

## Technical Stack

- Frontend: Vue3 + TypeScript + Element Plus
- Backend: Python 3.11, Django 4.2, Django REST Framework, Celery, LangChain
- Database: PostgreSQL + pgvector

## Project Highlights

- All core modules (knowledge base, model integration, API, etc.) are independently designed and implemented by <b>Yuelinfeng</b>.
- Not a fork of MaxKB or any other project.
- Focus on code quality, extensibility, and real-world programming scenarios.

## License

This project is licensed under GPLv3.  
Copyright (c) 2024 Yuelinfeng.

Contact: 2021214376@stu.cqupt.edu.cn

---

Welcome to star and contact for collaboration or suggestions!

