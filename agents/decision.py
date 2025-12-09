from llm_hf import hf_generate

def decision_agent(user_input):
    prompt = f"""
You are the Decision Helper Agent.
Use this framework:
1. Options
2. Pros
3. Cons
4. Emotional view
5. Logical view
6. Recommendation style (non-forceful)

User message:
{user_input}

Respond:
"""
    return hf_generate(prompt)
