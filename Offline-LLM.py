from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st



# Page Configuration

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="centered"
)


# Custom CSS

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #777;
        margin-bottom: 2rem;
    }

    .stChatMessage {
        border-radius: 12px;
    }

    .model-status {
        padding: 10px 15px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)



# Header

st.markdown(
    '<div class="main-title"> AI Chat Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Powered by LangChain + Ollama</div>',
    unsafe_allow_html=True
)


# Sidebar

with st.sidebar:
    st.header(" Settings")

    model_name = st.selectbox(
        "Choose Model",
        [
            "gemma3:latest",
            "llama3.1"
        ]
    )

    st.divider()

    st.markdown("### About")
    st.write(
        "A lightweight local AI assistant built with "
        "LangChain and Ollama."
    )

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()



# Model

template = """
You are a helpful AI assistant.

Answer the user's question clearly and accurately.

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model=model_name)

chain = prompt | model



# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat Input

question = st.chat_input(
    " Ask me anything..."
)


if question:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = chain.invoke(
                    {"question": question}
                )

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                error_message = (
                    " Unable to connect to Ollama. "
                    "Make sure Ollama is running and the selected "
                    f"model `{model_name}` is available."
                )

                st.error(error_message)
                st.code(str(e))