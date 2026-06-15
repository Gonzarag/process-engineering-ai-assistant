from openai import OpenAI

from src.config import OPENAI_MODEL
from src.knowledge_base import get_topic_context
from src.prompts import SYSTEM_PROMPT

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


def ask_assistant(user_question: str, learning_mode: str = "Tutor") -> str:
    prompt = build_learning_prompt(user_question, learning_mode)

    response = client.responses.create(
        model=OPENAI_MODEL,
        reasoning={"effort": "medium"},
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
