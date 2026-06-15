import streamlit as st

from src.assistant import ask_assistant

st.set_page_config(
    page_title="Process Engineering AI Assistant",
    page_icon="⚙️",
    layout="centered",
)

st.title("⚙️ Process Engineering AI Learning Assistant")

st.write(
    """
Ask questions about process engineering, industrial data analysis,
automation, anomaly detection, prediction models, and optimization.
"""
)

learning_mode = st.sidebar.selectbox(
    "Learning mode",
    [
        "Tutor",
        "Quiz generator",
        "Worked example",
        "Interview preparation",
        "Industrial application",
        "Roadmap builder",
    ],
)

st.sidebar.markdown("## Suggested topics")
st.sidebar.markdown(
    """
- Mass balances  
- Energy balances  
- Fluid flow  
- Heat transfer  
- Distillation  
- Process control  
- Process safety  
- Industrial data analysis  
- Anomaly detection  
- Prediction models  
- Optimization  
"""
)

question = st.text_area(
    "Your question",
    placeholder="Example: Explain mass balances with a tank example.",
    height=120,
)

if st.button("Ask assistant"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            try:
                answer = ask_assistant(question, learning_mode)
                st.markdown(answer)
            except Exception as error:
                st.error(f"Something went wrong: {error}")
