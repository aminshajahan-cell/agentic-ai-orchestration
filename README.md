# 🧠 Agentic AI – Multi-Agent Orchestration (Python)

Multi-agent orchestration using Microsoft Agent Framework and GitHub Models.

---

## 🚀 Overview

This project demonstrates **Agentic AI** using a **multi-agent orchestration pattern** instead of a single monolithic AI.

Each agent has a **clear responsibility**, and an **orchestrator** manages how tasks move from one agent to another — similar to how real teams work.

This is a practical, beginner-friendly implementation focused on **clarity and design patterns**, not hype.

---

## 🧩 Architecture (High Level)

User Input (CLI)
↓
Planner Agent
↓
Executor Agent
↓
Reviewer Agent
↓
Final Output


The **orchestrator** controls:
- Agent execution order
- Handoff between agents
- Final response aggregation

---

## 🤖 Agents & Roles

### 🧠 Planner Agent (Support Agent)
- Understands the user request
- Breaks the task into clear steps
- Decides *what needs to be done*

### ⚙️ Executor Agent
- Executes the planned steps
- Generates the main response
- Calls tools when required

### 🔍 Reviewer Agent
- Reviews the generated output
- Improves clarity and correctness
- Reduces hallucinations or ambiguity

Each agent runs with its own **system message** (role-based prompting).

---

## 🛠️ Tools & RAG Concept

Agents **do not directly access data**.

Instead:
- Tools act like **functions**
- Tools may search knowledge bases, tickets, or files
- Retrieved data is passed back to the agent
- The agent generates responses using **RAG (Retrieval-Augmented Generation)**

This improves:
- Accuracy  
- Reliability  
- Explainability  

---

## 🧪 How to Run

### 1️⃣ Activate virtual environment
```powershell
.\.venv\Scripts\Activate.ps1
