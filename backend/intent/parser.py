from backend.config import client, MODEL
from backend.intent.examples import FEW_EXAMPLES
from backend.intent.schema import SCHEMA
import json

def is_db_query(user_query):
    """
    Detect whether query should go to phone_details DB.
    """
    keywords = [
        # General phone terms
        "phone", "mobile", "smartphone", "device",

        # Brands (add more as needed)
        "oppo", "blackberry", "microsoft", "htc", "land", "lg", "fly", "oukitel", "ioutdoor", "myphone", "s-tell", "zte", "sharp", "huawei", "umidigi", "nuu", "maxcom", "philips", "blackview", "vivo", "motorola", "doogee", "bravis", "viaan", "xiaomi", "vernee", "2e", "sony", "coolpad", "google", "keneksi", "meizu", "tecno", "agm", "realme", "elephone", "honor", "nomi", "jinga", "astro", "cubot", "ulefone", "oneplus", "vodafone", "lenovo", "globex", "smartex", "apple", "cat", "assistant", "rezone", "prestigio", "archos", "asus", "bluboo", "nokia", "ergo", "crosscall", "mafam", "samsung", "alcatel", "sigma mobile", "leagoo", "general",
        
        # models
        "galaxy"

        # Pricing
        "price", "cost", "cheapest", "best price",
        "lowest", "highest", "under", "below", "above",

        # Specs
        "battery", "screen", "display", "memory", "ram",
        "storage", "size",

        # OS
        "android", "ios",

        # Popularity / sellers
        "popular", "popularity", "seller", "sellers",

        # Query intent
        "list", "show", "compare", "find", "which", "top"
    ]

    uq = user_query.lower()
    is_db = any(keyword in uq for keyword in keywords)

    print(f"DEBUG: is_db_query('{user_query[:40]}...') -> {is_db}")
    return is_db


def query_to_intent(user_query):
    prompt = SCHEMA + "\n\n"
    # print("1: ", prompt)
    for ex in FEW_EXAMPLES:
        prompt += f"User: {ex['user']}\nOutput: {json.dumps(ex['json'])}\n\n"
        # print("2: ", prompt)

    # print("3: ", prompt)

    prompt += (
        f"User: {user_query}\n"
        "Output ONLY valid JSON. No explanation. No markdown."
    )
    # print("4: ", prompt)

    print("DEBUG: Sending prompt to model for intent parsing (truncated)...")
    # NOTE: if you hit rate limits or want to test offline, replace this with a mock.
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    print("\nDEBUG: RAW LLM OUTPUT (intent):", raw)
    try:
        intent = json.loads(raw)
    except Exception as e:
        print("ERROR: Failed to parse JSON intent:", e)
        # Return a safe unknown intent
        return {"action": "unknown", "reason": "Failed to parse intent JSON."}

    print("DEBUG: Parsed intent:", intent)
    return intent

# intent = query_to_intent("give me details about doogee Y9 Plus")
# print(intent)