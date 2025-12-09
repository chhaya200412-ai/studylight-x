from llm_hf import hf_generate

def emotional_agent(user_input):
    prompt = f"""
You are the Emotional Wellness Agent.
Speak warmly, gently, safely.
No medical advice.

User message:
{user_input}

Respond:
"""
    return hf_generate(prompt)
