# MasRouter Research Implementation
A lightweight research implementation inspired by **MasRouter: Learning to Route LLMs for Multi-Agent Systems**.
This project implements a simplified MasRouter-style multi-agent routing pipeline using:
- Task classification
- Collaboration mode selection
- Agent role allocation
- LLM routing
- Multi-agent execution using Gemini API
The current working pipeline successfully routes a coding query into a `Programmer → Tester → Verifier` chain and generates a final verified answer. 
## Project Goal
The goal of this project is to explore **cost-aware LLM routing for multi-agent systems**.
Instead of using one large model for every task, the system decides:
1. What type of task the query is
2. Which collaboration mode should be used
3. Which agents are needed
4. Which LLM should power each agent
5. How the final answer should be verified
## Current Architecture
```text
User Query
   |
   v
MasRouter
   |
   |-- Task Classifier
   |-- Collaboration Mode Selector
   |-- Role Allocator
   |-- LLM Router
   |
   v
Multi-Agent Execution
   |
   |-- Programmer Agent
   |-- Tester Agent
   |-- Verifier Agent
   |
   v
Final Answer
```
## Current Features
- Rule-based task classification
- Coding, math, research, and general task routing
- Dynamic role allocation
- Gemini API integration through LiteLLM
- Multi-agent chain execution
- Dry-run mode for checking routing without API call
- Final answer generation through verifier agent
## Tech Stack
```text
Python
LiteLLM
Google Gemini API
PyYAML
python-dotenv
PowerShell
GitHub
```
## Folder Structure
```text
MasRouter/
├── configs/
│   ├── models.yaml
│   └── routing.yaml
├── src/
│   ├── main.py
│   └── masrouter/
│       ├── __init__.py
│       ├── llm_client.py
│       ├── router.py
│       └── runner.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
## Setup
Clone the repository:
```powershell
git clone https://github.com/zrohan-enter/MasRouter-Research-Implementation.git
cd MasRouter-Research-Implementation
```
Create and activate virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
Install dependencies:
```powershell
pip install -r requirements.txt
```
Create environment file:
```powershell
copy .env.example .env
notepad .env
```
Add your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
Do not upload `.env` to GitHub.
## Dry Run
Dry run checks the routing plan without calling the API.
```powershell
python .\src\main.py --query "Write a Python function to check prime number" --dry-run
```
Example routing output:
```json
{
  "task_type": "coding",
  "collaboration_mode": "Chain",
  "agents": [
    {
      "role": "Programmer",
      "llm": "gemini/gemini-2.5-flash"
    },
    {
      "role": "Tester",
      "llm": "gemini/gemini-2.5-flash"
    },
    {
      "role": "Verifier",
      "llm": "gemini/gemini-2.5-flash"
    }
  ]
}
```
## Real Run
This runs the actual multi-agent system.
```powershell
python .\src\main.py --query "Write a Python function to check prime number"
```
Expected flow:
```text
Programmer Agent → writes solution
Tester Agent → checks correctness and edge cases
Verifier Agent → prepares final clean answer
```
## Research Direction
This project is currently a **rule-based MasRouter MVP**.
Future improvements:
- Add token counting
- Add cost tracking
- Add benchmark evaluation
- Add GSM8K, HumanEval, and MBPP sample tests
- Replace rule-based router with trainable router
- Add Sentence-BERT or MiniLM embeddings
- Add cost-performance optimization
- Compare single-agent vs multi-agent performance
- Compare fixed routing vs adaptive routing
## Paper Inspiration
This project is inspired by the MasRouter paper, which proposes routing for multi-agent systems by selecting:
- Collaboration mode
- Agent roles
- LLM backbone for each agent
The original paper focuses on improving performance while reducing inference cost.
## Security Note
Never commit API keys.
The following files are intentionally ignored:
```text
.env
.venv/
__pycache__/
models/
datasets/
cache/
logs/
wandb/
```
## Repository
```text
https://github.com/zrohan-enter/MasRouter-Research-Implementation
```
## Status
Current status: Working MVP completed.
The system can successfully:
- classify a task
- select collaboration mode
- allocate agents
- assign LLMs
- run Gemini-powered multi-agent execution
- produce final verified output

## Tested Results

A tested sample output is available in the `results/` folder.

```text
results/sample_prime_test_output.txt
```

This output proves the working MasRouter pipeline:

```text
Query -> Router Plan -> Programmer Agent -> Tester Agent -> Verifier Agent -> Final Answer
```

The tested query was:

```text
Write a Python function to check prime number
```

Additional tested output:

```text
results/sample_math_test_output.txt
```
