from litellm import completion
def call_llm(model: str, system_prompt: str, user_prompt: str):
    response = completion(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]
