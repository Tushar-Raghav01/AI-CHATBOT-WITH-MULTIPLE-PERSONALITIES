
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st


# -------------------- Configuration --------------------

load_dotenv()

st.set_page_config(
    page_title="AI Persona Chat",
    page_icon="🤖",
    layout="wide"
)


# -------------------- Custom Styling --------------------

st.markdown("""
<style>

    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827, #1e1b4b);
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #a5b4fc;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .persona-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 20px;
    }

    .chat-container {
        background: rgba(255,255,255,0.04);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .user-message {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        padding: 13px 18px;
        border-radius: 18px 18px 4px 18px;
        margin: 10px 0 10px 20%;
    }

    .bot-message {
        background: rgba(255,255,255,0.09);
        color: #f8fafc;
        padding: 13px 18px;
        border-radius: 18px 18px 18px 4px;
        margin: 10px 20% 10px 0;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .message-name {
        font-size: 12px;
        font-weight: 700;
        opacity: 0.7;
        margin-bottom: 5px;
    }

</style>
""", unsafe_allow_html=True)


# -------------------- Model --------------------

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)


# -------------------- Session State --------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = ""

if "started" not in st.session_state:
    st.session_state.started = False


# -------------------- Header --------------------

st.markdown(
    '<div class="main-title">🤖 AI Persona Chat</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your AI personality and start chatting</div>',
    unsafe_allow_html=True
)


# -------------------- Sidebar --------------------

with st.sidebar:

    st.markdown("## 🎭 Choose Your Mode")

    choose = st.radio(
        "Select personality",
        [
            "👨‍🏫 AI Teacher",
            "🤝 Friend",
            "😡 Angry Person",
            "😢 Sad Person"
        ]
    )

    st.divider()

    if choose == "👨‍🏫 AI Teacher":
        mode = "you are an ai teacher"

    elif choose == "🤝 Friend":
        mode = "you are a friend"

    elif choose == "😡 Angry Person":
        mode = "you are an angry person"

    else:
        mode = "you are a sad person"

    st.markdown("### Current Mode")

    st.info(choose)

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.messages = []
        st.session_state.mode = mode

        st.rerun()


# -------------------- Initialize System Message --------------------

if not st.session_state.messages:

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

    st.session_state.mode = mode


# -------------------- Mode Change --------------------

if st.session_state.mode != mode:

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

    st.session_state.mode = mode


# -------------------- Chat Area --------------------

st.markdown(
    '<div class="chat-container">',
    unsafe_allow_html=True
)

# Display previous messages

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        st.markdown(
            f"""
            <div class="user-message">
                <div class="message-name">YOU</div>
                {message.content}
            </div>
            """,
            unsafe_allow_html=True
        )

    elif isinstance(message, AIMessage):

        st.markdown(
            f"""
            <div class="bot-message">
                <div class="message-name">AI</div>
                {message.content}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)


# -------------------- User Input --------------------

prompt = st.chat_input("Type your message...")


if prompt:

    # Same logic as your original code
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Get response using complete history
    response = model.invoke(
        st.session_state.messages
    )

    # Store AI response in history
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    st.rerun()
