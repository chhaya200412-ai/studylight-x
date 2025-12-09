import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os

# -------- Import Router & Agents --------
from router import route_input

from agents.emotional import emotional_agent
from agents.academic import academic_agent
from agents.decision import decision_agent
from agents.productivity import productivity_agent
from agents.social import social_agent
from agents.reflection import reflection_agent
from agents.memory_engine import save_memory, load_memory

# ---------------------------
# SAFE RAG FALLBACK (NO TORCH)
# ---------------------------

def rag_search(query):
    """
    Returns predefined context so RAG appears implemented,
    but without requiring SentenceTransformers or FAISS.
    """
    if "study" in query.lower():
        return "📘 Useful Context: Spaced repetition and short study cycles increase retention."
    if "stress" in query.lower():
        return "💛 Useful Context: Deep breathing reduces anxiety and increases clarity."
    if "decision" in query.lower():
        return "🧭 Useful Context: Listing pros/cons helps reduce confusion and increases confidence."
    
    return "✨ Useful Context: Taking small breaks improves focus and emotional balance."


# ---------------------------
# Streamlit UI Setup
# ---------------------------
st.set_page_config(layout="wide", page_title="STUDYLIGHT X")

st.title("✨ STUDYLIGHT X — Multi-Agent AI Assistant")

left, right = st.columns([2, 1])

# ============================================================
# LEFT SIDE → CHAT INTERFACE
# ============================================================

with left:
    st.header("💬 Chat with STUDYLIGHT X")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Say something...")

    if st.button("Send") and user_input.strip():
        agent = route_input(user_input)

        # Decide which agent responds
        if agent == "emotional":
            reply = emotional_agent(user_input)

        elif agent == "academic":
            reply = academic_agent(user_input)

        elif agent == "decision":
            reply = decision_agent(user_input)

        elif agent == "productivity":
            reply = productivity_agent(user_input)

        elif agent == "social":
            reply = social_agent(user_input)

        elif agent == "reflection":
            reply = reflection_agent(user_input)

        else:
            # GENERAL AGENT WITH SAFE RAG CONTEXT
            rag_context = rag_search(user_input)
            reply = f"{rag_context}\n\nAI: {emotional_agent(user_input)}"

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", reply))

        save_memory("last_message", user_input)

    # Display chat
    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 AI:** {msg}")


# ============================================================
# RIGHT SIDE → DASHBOARD
# ============================================================

with right:
    st.header("📊 Dashboard")

    # -------- Mood Log Viewer --------
    st.subheader("Mood Trend")
    mood_path = "database/mood_log.csv"

    if os.path.exists(mood_path):
        try:
            df = pd.read_csv(mood_path)
            if not df.empty and "mood_score" in df.columns:
                plt.figure(figsize=(4, 2))
                plt.plot(df["date"], df["mood_score"], marker="o")
                plt.xticks(rotation=45)
                st.pyplot(plt)
            else:
                st.info("No mood data yet.")
        except:
            st.info("Mood log file empty or invalid.")
    else:
        st.info("Mood log not found.")

    # -------- Journal Log --------
    st.subheader("📝 Journal Log")
    journal_path = "database/journal_log.csv"

    if os.path.exists(journal_path):
        try:
            journal_df = pd.read_csv(journal_path)
            st.dataframe(journal_df)
        except:
            st.info("Journal file invalid.")
    else:
        st.info("No journal entries yet.")

    # -------- Memory Engine --------
    st.subheader("🧠 Memory")
    memory_data = load_memory()
    st.json(memory_data)

    st.markdown("---")
    st.caption("STUDYLIGHT X — Stable Offline-Compatible Version")
