from llm_hf import hf_generate

def reflection_agent(user_input):
    prompt = f"""
You are the Reflection & Journaling Agent.
Encourage awareness, clarity, gratitude.

User:
{user_input}

Ask 2 reflective questions:
"""
    return hf_generate(prompt)
