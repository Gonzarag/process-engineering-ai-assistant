# Architecture

## Purpose

The application is designed as a lightweight AI learning assistant for process engineering.

## Main Components

### Streamlit Interface

The user interacts with the assistant through a Streamlit web app.

### Assistant Service

The assistant service receives the user question, adds learning mode context, retrieves relevant process engineering topic context, and sends the prompt to the OpenAI API.

### Prompt Layer

The prompt layer defines the tutor behavior, response format, safety rules, and teaching style.

### Knowledge Base

The knowledge base contains short curated summaries of common process engineering topics.

## Data Flow

```text
User question
→ Streamlit app
→ Assistant service
→ Prompt builder
→ OpenAI Responses API
→ Model response
→ Streamlit display
