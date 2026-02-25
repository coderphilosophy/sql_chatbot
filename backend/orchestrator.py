# GRADIO VERSION OF ORCHESTRATOR.PY - IGNORE

# from backend.intent.parser import *
# from backend.execution.runner import *
# from backend.execution.normalizer import *
# from backend.fallback.evaluator import *
# from backend.fallback.rules import *
# from backend.llm.client import *
# from backend.db import db

# def ask(user_query, history):
#     print("\n========== ORCHESTRATOR START ==========")
#     print("DEBUG: User Query:", user_query)

#     # # 1️⃣ ROUTER
#     if not is_db_query(user_query):
#         print("DEBUG: Routed to pure chat mode")
#         return chat_llm(user_query)

#     print("DEBUG: Routed to DB pipeline")

#     # 2️⃣ INTENT PARSING
#     intent = query_to_intent(user_query)
#     intent = normalize_intent(intent)
    
#     if intent.get("action") == "unknown":
#         print("DEBUG: Intent unknown → returning reason")
#         return intent.get(
#             "reason",
#             "I don’t have information about this."
#         )

#     # 3️⃣ ORM QUERY EXECUTION
#     try:
#         db_result = run_intent(db, intent)
#     except Exception as e:
#         print("ERROR: ORM execution failed:", str(e))
#         return f"Error: Failed to query database – {str(e)}"

#     # 4️⃣ RESULT EVALUATION
#     evaluation = result_evaluator(db_result, intent)

#     # 5️⃣ NORMAL FLOW
#     if evaluation["status"] == "ok":
#         # Convert ORM objects → dicts (only requested columns)
#         data = [
#             {col: getattr(row, col) for col in intent["columns"]}
#             for row in evaluation["data"]
#         ]

#         message = f"""
# User asked: {user_query}
# Database result: {data}
# Intent: {intent}

# Explain this clearly and concisely.
# """
#         explanation = chat_llm(message)
#         print("========== FINAL (NORMAL) ==========")
#         return explanation

#     # 6️⃣ FALLBACK FLOW
#     else:
#         fallback_text = get_fallback_message(
#             intent,
#             evaluation["reason"]
#         )

#         message = f"""
# User asked: {user_query}
# {fallback_text}

# Explain this as helpful guidance.
# Do NOT hallucinate.
# """
#         explanation = chat_llm(message)
#         print("========== FINAL (FALLBACK) ==========")
#         return explanation


# NEXT JS VERSION

from backend.intent.parser import *
from backend.execution.runner import *
from backend.execution.normalizer import *
from backend.fallback.evaluator import *
from backend.fallback.rules import *
from backend.llm.client import *
from backend.db import db


def ask(user_query: str) -> dict:
    print("\n========== ORCHESTRATOR START ==========")
    print("DEBUG: User Query:", user_query)

    # ROUTER
    if not is_db_query(user_query):
        print("DEBUG: Routed to pure chat mode")
        answer = chat_llm(user_query)
        return {
            "answer": answer,
            "sql": None,
            "data": None
        }

    print("DEBUG: Routed to DB pipeline")

    # INTENT PARSING
    intent = query_to_intent(user_query)
    intent = normalize_intent(intent)

    if intent.get("action") == "unknown":
        print("DEBUG: Intent unknown")
        return {
            "answer": intent.get(
                "reason",
                "I don’t have information about this."
            ),
            "sql": None,
            "data": None
        }

    # ORM QUERY EXECUTION
    try:
        db_result = run_intent(db, intent)
    except Exception as e:
        print("ERROR: ORM execution failed:", str(e))
        return {
            "answer": f"Failed to query database: {str(e)}",
            "sql": None,
            "data": None
        }

    #  RESULT EVALUATION
    evaluation = result_evaluator(db_result, intent)

    # NORMAL FLOW
    if evaluation["status"] == "ok":
        data = [
            {col: getattr(row, col) for col in intent["columns"]}
            for row in evaluation["data"]
        ]

        prompt = f"""
User asked: {user_query}
Database result: {data}
Intent: {intent}

Explain this clearly and concisely.
"""
        explanation = chat_llm(prompt)

        print("========== FINAL (NORMAL) ==========")

        return {
            "answer": explanation,
            "sql": intent.get("sql"),  # optional if you store it
            "data": data
        }

    # FALLBACK FLOW
    fallback_text = get_fallback_message(
        intent,
        evaluation["reason"]
    )

    prompt = f"""
User asked: {user_query}
{fallback_text}

Explain this as helpful guidance.
Do NOT hallucinate.
"""
    explanation = chat_llm(prompt)

    print("========== FINAL (FALLBACK) ==========")

    return {
        "answer": explanation,
        "sql": None,
        "data": None
    }
