import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os
import re
import json

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize model
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    groq_api_key=groq_api_key,
    temperature=1
)

# Function to clean <think> tags
def remove_think_tags(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

# Convert messages to JSON
def export_chat_json(messages):
    export_data = []
    for msg in messages:
        role = "system"
        if isinstance(msg, HumanMessage):
            role = "user"
        elif isinstance(msg, AIMessage):
            role = "assistant"
        export_data.append({"role": role, "content": msg.content})
    return json.dumps(export_data, indent=2)

# Convert messages to Markdown
def export_chat_markdown(messages):
    md_text = ""
    for msg in messages:
        if isinstance(msg, HumanMessage):
            md_text += f"**You:** {msg.content}\n\n"
        elif isinstance(msg, AIMessage):
            md_text += f"**AI:** {msg.content}\n\n"
    return md_text

# Streamlit app
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 AI Chatbot (Groq + Streamlit)")
st.write("Chat with the DeepSeek model via Groq API")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="You are a helpful assistant.")]

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# User input
if user_input := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Model response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = llm.invoke(st.session_state.messages)
            clean_output = remove_think_tags(result.content)
            st.markdown(clean_output)

    # Save assistant message
    st.session_state.messages.append(AIMessage(content=clean_output))

# --- Export Chat History ---
st.sidebar.header("📂 Export Chat")
st.sidebar.download_button(
    "⬇️ Download as JSON",
    data=export_chat_json(st.session_state.messages),
    file_name="chat_history.json",
    mime="application/json"
)
st.sidebar.download_button(
    "⬇️ Download as Markdown",
    data=export_chat_markdown(st.session_state.messages),
    file_name="chat_history.md",
    mime="text/markdown"
)
