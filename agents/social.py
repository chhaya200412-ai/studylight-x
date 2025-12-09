from llm_hf import hf_generate

def social_agent(user_input):
    prompt = f"""
You are the Social Skills Agent.
Help with communication, conflict, friendship.

User:
{user_input}

Give a script + guidance:
"""
    return hf_generate(prompt)
