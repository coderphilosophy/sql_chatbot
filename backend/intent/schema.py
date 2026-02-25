SCHEMA = """
Tables:
PhoneDetail(
    id:int,
    brand_name:string
    model_name:string
    os:string
    popularity:int
    best_price:float
    sellers_amount:int
    screen_size:float
    memory_size:float
    battery_size:float
    release_date:string
)

Rules:
- Output ONLY JSON.
- Keys MUST be: action, columns, table, filters, group_by, limit, join.
- Use EXACT table and column names. No hallucination.
- If query cannot be answered using these tables, return:
  {"action":"unknown","reason":"I don't have information about this."}
- Do NOT generate SQL.
"""
