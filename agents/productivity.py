from llm_hf import hf_generate

def productivity_agent(user_input):
    prompt = f"""
You are the Productivity Agent.
Give focus tips, planning, energy methods.

User:
{user_input}

Give clear steps:
"""
    return hf_generate(prompt)
