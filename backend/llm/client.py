from backend.config import client, MODEL

SYSTEM_PREFIX = """
You are a reliable and precise Mall Operations Assistant.

Your job:
- Explain database results clearly.
- Do NOT invent facts or data not present.
- When DB results are missing and fallback text is provided,
  present it politely as guidance for a mall manager.
- Keep answers short, helpful, professional.

Rules:
- Never hallucinate machine names, item names, quantities, or locations.
- Only describe exactly what the DB result or fallback message says.
"""

def chat_llm(message):
    """
    Send message to LLM-B to produce natural language explanation.
    """
    print("DEBUG: Sending to LLM-B (for wording). Message preview:", message[:200])
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PREFIX},
            {"role": "user", "content": message}
        ],
        temperature=0.7
    )
    out = response.choices[0].message.content
    print("DEBUG: LLM-B returned (truncated):", out[:300])
    return out

def format_db_results_for_llm(user_query, result, intent):
    """
    Create a short context string describing DB results for LLM to explain to user.
    Keep it literal to avoid hallucination.
    """
    return f"User asked: {user_query}\nDB Results (literal): {result}\nIntent: {intent}\nPlease explain these results simply and concisely. Do NOT add facts not in DB."
