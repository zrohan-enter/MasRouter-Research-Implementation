from masrouter.llm_client import call_llm
def build_system_prompt(role: str):
    role_lower = role.lower()
    if "programmer" in role_lower:
        return (
            "You are the Programmer agent. Write the actual solution/code clearly. "
            "Include clean code, explanation, and examples if needed."
        )
    if "tester" in role_lower:
        return (
            "You are the Tester agent. Test the previous solution logically. "
            "Find bugs, edge cases, and suggest corrections. Do not only approve."
        )
    if "verifier" in role_lower:
        return (
            "You are the Verifier agent. Produce the final answer for the user. "
            "Use the Programmer and Tester outputs, fix any issues, and include the final clean code. "
            "Do not only say approved."
        )
    return f"You are a {role} in a multi-agent research system. Complete your role carefully."
def run_mas(query, plan):
    current_context = query
    outputs = []
    for agent in plan["agents"]:
        role = agent["role"]
        model = agent["llm"]
        system_prompt = build_system_prompt(role)
        user_prompt = f"""
Original user query:
{query}
Previous context and agent outputs:
{current_context}
Now complete your role as: {role}
"""
        answer = call_llm(model, system_prompt, user_prompt)
        outputs.append({
            "role": role,
            "model": model,
            "answer": answer
        })
        current_context += f"\n\n[{role} output]\n{answer}"
    final_answer = outputs[-1]["answer"] if outputs else ""
    return final_answer, outputs
