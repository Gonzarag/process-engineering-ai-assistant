import os

from openai import OpenAI

from src.config import OPENAI_MODEL
from src.knowledge_base import get_topic_context
from src.prompts import SYSTEM_PROMPT

APP_MODE = os.getenv("APP_MODE", "demo").lower()

client = OpenAI()


def build_learning_prompt(user_question: str, learning_mode: str) -> str:
    topic_context = get_topic_context(user_question)

    return f"""
Learning mode: {learning_mode}

Relevant process engineering context:
{topic_context}

User question:
{user_question}

Please answer as a process engineering learning assistant.
"""


def demo_response(user_question: str, learning_mode: str) -> str:
    topic_context = get_topic_context(user_question)

    return f"""
## Demo Mode Response

This is a local demo response. No OpenAI API call was made.

## Learning Mode

{learning_mode}

## Your Question

{user_question}

## Process Engineering Context

{topic_context}

## Example Answer Structure

### 1. Concept

This topic can be explained using basic process engineering principles and industrial examples.

### 2. Why It Matters in Industry

Understanding this concept helps engineers monitor performance, reduce inefficiencies, improve safety, and support better decision-making.

### 3. Simple Example

Imagine a production unit where process data is collected every hour. By analyzing trends such as temperature, pressure, flow, quality, and downtime, engineers can identify abnormal behavior and improvement opportunities.

### 4. Practice Exercise

Create a small table with hourly process data and identify one trend, one abnormal value, and one possible engineering explanation.

### 5. Next Learning Step

Replace demo mode with API mode once billing/quota is available, then compare AI-generated answers with your own engineering interpretation.
"""


def ask_assistant(user_question: str, learning_mode: str = "Tutor") -> str:
    if APP_MODE == "demo":
        return demo_response(user_question, learning_mode)

    prompt = build_learning_prompt(user_question, learning_mode)

    response = client.responses.create(
        model=OPENAI_MODEL,
        reasoning={"effort": "low"},
        text={"verbosity": "medium"},
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.output_text