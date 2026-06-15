def test_import_prompts():
    from src.prompts import SYSTEM_PROMPT

    assert "process engineering" in SYSTEM_PROMPT.lower()


def test_import_knowledge_base():
    from src.knowledge_base import get_topic_context

    context = get_topic_context("mass balances")
    assert "mass balances" in context.lower()
