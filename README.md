# AI-Powered Process Engineering Learning Assistant

## Overview

This project is an AI-powered learning assistant focused on **process engineering, industrial automation, process optimization, and applied AI**.

The assistant helps learners understand engineering concepts through structured explanations, industrial examples, quizzes, worked examples, and learning roadmaps.

---

## Project Goals

The goal of this project is to demonstrate how AI can support engineering education and professional development.

The assistant is designed to help users learn topics such as:

* Mass balances
* Energy balances
* Fluid flow
* Heat transfer
* Distillation
* Process control
* Process safety
* Industrial data analysis
* Process anomaly detection
* Prediction models
* Industrial optimization

---

## Features

* Ask process engineering questions
* Generate beginner-friendly explanations
* Create quizzes
* Produce worked examples
* Suggest learning roadmaps
* Connect theory with industrial applications
* Support AI and automation learning for process engineers

---

## Architecture

```text
User
 │
 ▼
Streamlit Web App
 │
 ▼
Assistant Service
 │
 ├── Prompt builder
 ├── Process engineering context
 ├── Tutor behavior instructions
 └── OpenAI API call
        │
        ▼
OpenAI Model
        │
        ▼
Structured learning response
```

---

## Repository Structure

```text
process-engineering-ai-assistant/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── app.py
├── src/
│   ├── assistant.py
│   ├── config.py
│   ├── prompts.py
│   └── knowledge_base.py
├── docs/
├── examples/
├── tests/
└── assets/
    └── screenshots/
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/process-engineering-ai-assistant.git
cd process-engineering-ai-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/Scripts/activate
```

Or on Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.5
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## Example Questions

```text
Explain mass balances using a tank example.
```

```text
Create a quiz about heat exchangers.
```

```text
Explain anomaly detection for industrial sensor data.
```

```text
Build a roadmap to learn process control and AI.
```

---

## Screenshots

Add screenshots here after running the app.

```markdown
![Assistant screenshot](assets/screenshots/app-screenshot.png)
```

---

## Documentation

Additional documentation:

* `docs/architecture.md`
* `docs/user-guide.md`
* `docs/prompt-design.md`

---

## Safety and Limitations

This assistant is intended for educational use.

It should not be used as the only source for real plant operation, process safety decisions, control system changes, equipment design, or compliance work. Real industrial decisions require qualified engineering review and applicable standards.

---

## Future Improvements

* Add chat history
* Add topic-specific learning paths
* Add downloadable quiz outputs
* Add user progress tracking
* Add retrieval from curated engineering notes
* Add diagrams and formula explanations
* Add Streamlit Cloud deployment
* Add evaluation tests for answer quality

---

## Portfolio Value

This project demonstrates:

* Python development
* OpenAI API integration
* Prompt engineering
* Streamlit app development
* Process engineering knowledge
* AI-assisted learning design
* Documentation and GitHub project organization
