from llm_hf import hf_generate

def academic_agent(user_input):
    prompt = f"""
You are the Academic Planning Agent.
Help with study plans, assignments, exams.

User message:
{user_input}

Respond step-by-step:
"""
    return hf_generate(prompt)
