from backend.fallback.rules import fallback_actions

def result_evaluator(db_result, intent):
    """
    Evaluates ORM DB results:
    - If empty → fallback
    - If requested fields are NULL → fallback
    """
    print("DEBUG: Evaluating DB result for fallback...")

    # Case 1: No rows
    if not db_result or len(db_result) == 0:
        print("DEBUG: No rows returned → fallback")
        return {
            "status": "fallback",
            "reason": "no_data",
            "data": db_result
        }

    requested_columns = intent.get("columns", [])

    # Case 2: NULL values in requested columns
    for row in db_result:
        for col in requested_columns:
            value = getattr(row, col, None)
            if value is None:
                print(f"DEBUG: NULL detected → {col}")
                return {
                    "status": "fallback",
                    "reason": "null_values",
                    "data": db_result
                }

    print("DEBUG: DB result OK → normal flow")
    return {
        "status": "ok",
        "reason": None,
        "data": db_result
    }


def get_fallback_message(intent, reason):
    table = intent.get("table")

    msg = fallback_actions.get(table, fallback_actions["default"])

    final_msg = f"Fallback Reason: {reason}. {msg}"
    print("DEBUG: Fallback message prepared:", final_msg)
    return final_msg
