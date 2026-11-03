import streamlit as st
import requests

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Sidd AI | Hot Studio",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

WEBHOOK_URL = "https://siddpatel.app.n8n.cloud/webhook/b88cc008-6b2b-457e-82fa-d1a4224fa2cb"

# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "total_requests" not in st.session_state:
    st.session_state.total_requests = 0

# ==========================================
# SUPER HOT DESIGN
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@600;700&display=swap');

:root {
    --pink: #ff2e77;
    --orange: #ff7a1a;
    --yellow: #ffd23f;
    --purple: #8b2cff;
    --cyan: #22e4ff;
}

/* ---------- BACKGROUND ---------- */
.stApp {
    background:
        radial-gradient(circle at 10% 15%, rgba(255,46,119,0.45), transparent 32%),
        radial-gradient(circle at 90% 25%, rgba(139,44,255,0.45), transparent 36%),
        radial-gradient(circle at 50% 100%, rgba(255,122,26,0.35), transparent 42%),
        #05030a;
    background-attachment: fixed;
    color: #fff;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] { display: none; }
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 1100px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* ---------- BRAND ---------- */
.brand {
    text-align: center;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 7px;
    background: linear-gradient(90deg, var(--pink), var(--orange), var(--yellow), var(--pink));
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 5s linear infinite;
    padding: 10px;
}

@keyframes shine {
    to { background-position: 300% center; }
}

/* ---------- HERO ---------- */
.hero {
    text-align: center;
    padding: 30px 15px 44px;
}

.hero-icon {
    font-size: 84px;
    animation: bounce 2s ease-in-out infinite;
    filter: drop-shadow(0 0 22px var(--pink)) drop-shadow(0 0 45px var(--orange));
}

@keyframes bounce {
    0%, 100% { transform: translateY(0) rotate(-4deg); }
    50% { transform: translateY(-14px) rotate(4deg); }
}

.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(40px, 6.5vw, 72px);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.02;
    background: linear-gradient(90deg, #ff2e77, #ff7a1a, #ffd23f, #ff2e77);
    background-size: 250% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3.5s linear infinite;
    filter: drop-shadow(0 0 18px rgba(255,46,119,0.5));
}

.hero p {
    color: #d8c8ef;
    font-size: 16px;
    line-height: 1.7;
    max-width: 580px;
    margin: 16px auto 0;
}

/* ---------- STATUS PILL ---------- */
.online {
    display: inline-block;
    color: #fff;
    background: linear-gradient(90deg, #ff2e77, #ff7a1a);
    border-radius: 30px;
    padding: 9px 20px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    box-shadow: 0 0 25px rgba(255,46,119,0.75);
    animation: pulse 1.8s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 0 18px rgba(255,46,119,0.6); }
    50% { box-shadow: 0 0 36px rgba(255,122,26,0.95); }
}

/* ---------- SECTION HEADING ---------- */
.heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #fff;
    margin: 32px 0 18px;
    text-shadow: 0 0 14px rgba(255,46,119,0.6);
}

.heading::before {
    content: "🔥 ";
}

/* ---------- FEATURE CARDS ---------- */
.feature {
    position: relative;
    background: linear-gradient(145deg, rgba(255,46,119,0.18), rgba(139,44,255,0.14));
    border: 1px solid rgba(255,122,26,0.45);
    border-radius: 22px;
    padding: 22px;
    min-height: 160px;
    margin-bottom: 16px;
    backdrop-filter: blur(12px);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.feature:hover {
    transform: translateY(-8px) scale(1.03);
    border-color: var(--yellow);
    box-shadow: 0 20px 45px rgba(255,46,119,0.5), 0 0 30px rgba(255,210,63,0.25);
}

.feature-icon {
    font-size: 34px;
    filter: drop-shadow(0 0 10px var(--orange));
}

.feature h4 {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--yellow);
    font-size: 17px;
    margin: 12px 0 8px;
}

.feature p {
    color: #e3d6f5;
    font-size: 13px;
    line-height: 1.6;
}

/* ---------- CHAT PANEL (animated neon border) ---------- */
.chat-panel {
    background:
        linear-gradient(rgba(14,6,26,0.92), rgba(14,6,26,0.92)) padding-box,
        linear-gradient(90deg, #ff2e77, #ff7a1a, #ffd23f, #8b2cff, #ff2e77) border-box;
    background-size: auto, 300% 100%;
    animation: borderFlow 5s linear infinite;
    border: 2px solid transparent;
    border-radius: 26px;
    padding: 22px;
    margin: 30px 0 20px;
    box-shadow: 0 0 50px rgba(255,46,119,0.35);
}

@keyframes borderFlow {
    to { background-position: 0 0, 300% 0; }
}

/* ---------- CHAT MESSAGES ---------- */
div[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,46,119,0.35);
    border-radius: 20px;
    padding: 16px;
    margin-bottom: 14px;
    box-shadow: 0 0 20px rgba(255,46,119,0.12);
}

.stChatInput {
    border: 1px solid var(--pink) !important;
    border-radius: 18px !important;
    box-shadow: 0 0 22px rgba(255,46,119,0.45);
}

.stChatInput textarea {
    color: #fff !important;
}

/* ---------- BUTTONS ---------- */
.stButton button {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #ff2e77, #ff7a1a, #ffd23f);
    background-size: 200% 200%;
    border: none;
    border-radius: 16px;
    color: #fff;
    min-height: 48px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.3px;
    text-shadow: 0 1px 4px rgba(0,0,0,0.35);
    box-shadow: 0 8px 24px rgba(255,46,119,0.45);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stButton button:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 16px 36px rgba(255,122,26,0.7);
    color: #fff;
    border: none;
}

.stButton button:active {
    transform: scale(0.96);
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    color: #a594c4;
    font-size: 11px;
    letter-spacing: 1.5px;
    padding: 40px 0 10px;
}

.footer b {
    background: linear-gradient(90deg, var(--pink), var(--yellow));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="brand">✦ S I D D &nbsp; A I ✦</div>

<div style="text-align:center;">
    <span class="online">● SYSTEM ONLINE</span>
</div>

<div class="hero">
    <div class="hero-icon">🔥</div>
    <h1>Intelligence, Unleashed.</h1>
    <p>
        Your personal AI workspace to think, organize,
        automate and accomplish more. Bold ideas, zero boring. 💥
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# FEATURE CARDS
# ==========================================

st.markdown(
    '<div class="heading">Explore your AI workspace</div>',
    unsafe_allow_html=True
)

features = [
    ("📧", "Email Intelligence", "Read, summarize and reply to emails."),
    ("📅", "Smart Calendar", "Organize events and meetings."),
    ("✅", "Task Management", "Manage your daily priorities."),
    ("📝", "Smart Notes", "Capture important ideas instantly."),
    ("💰", "Expense Tracking", "Track spending and budgets."),
    ("🧠", "AI Assistant", "Ask questions and explore ideas.")
]

columns = st.columns(3)

for index, (icon, title, description) in enumerate(features):
    with columns[index % 3]:
        st.markdown(f"""
        <div class="feature">
            <div class="feature-icon">{icon}</div>
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# CHAT SECTION
# ==========================================

st.markdown("""
<div class="chat-panel">
    <div style="display:flex;align-items:center;gap:14px;">
        <div style="font-size:36px;filter:drop-shadow(0 0 10px #ffd23f);">⚡</div>
        <div>
            <div style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:20px;color:#fff;">
                Talk to Sidd AI
            </div>
            <div style="font-size:12px;color:#ffd23f;letter-spacing:0.5px;">
                Your intelligent personal assistant 😈
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# CHAT HISTORY
# ==========================================

for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# ==========================================
# SUGGESTED PROMPTS
# ==========================================

if not st.session_state.messages:

    st.caption("⚡ QUICK START")

    prompts = [
        "What can you do?",
        "Help me plan my day",
        "Summarize my emails",
        "Create a task"
    ]

    cols = st.columns(4)

    for i, prompt in enumerate(prompts):
        with cols[i]:
            if st.button(prompt, key=f"quick_{i}",
                         use_container_width=True):
                st.session_state.pending_prompt = prompt
                st.rerun()


# ==========================================
# CHAT INPUT
# ==========================================

typed_message = st.chat_input("Ask Sidd AI anything... 🔥")

user_message = typed_message

if not user_message:
    user_message = st.session_state.pop("pending_prompt", None)


# ==========================================
# N8N WEBHOOK INTEGRATION
# ==========================================

if user_message:

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Sidd AI is cooking... 🔥"):

            try:
                response = requests.post(
                    WEBHOOK_URL,
                    json={"message": user_message},
                    timeout=60
                )

                response.raise_for_status()

                data = response.json()

                # Preserve original n8n response structure
                if isinstance(data, list):
                    ai_response = data[0]["output"]
                else:
                    ai_response = data["output"]

                if not isinstance(ai_response, str):
                    raise ValueError("Invalid AI output")

                st.markdown(ai_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })

                st.session_state.total_requests += 1

            except requests.exceptions.Timeout:
                ai_response = "⏳ Server timed out. Please try again."
                st.error(ai_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })

            except requests.exceptions.RequestException as e:
                ai_response = f"⚠️ Connection error: {e}"
                st.error(ai_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })

            except (ValueError, KeyError, IndexError, TypeError):
                ai_response = "⚠️ Unexpected response from your AI server."
                st.error(ai_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })

    st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.markdown(f"""
<div class="footer">
    SIDD AI · PERSONAL INTELLIGENCE SYSTEM
    <br><br>
    TOTAL REQUESTS THIS SESSION: <b>{st.session_state.total_requests}</b>
    <br><br>
    POWERED BY STREAMLIT + N8N 🔥
</div>
""", unsafe_allow_html=True)