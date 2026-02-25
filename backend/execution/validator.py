from backend.models import PhoneDetail

MODEL_MAP = {
    "phone_details": PhoneDetail, 
}

ALLOWED_SCHEMA = {
    "phone_details": ["id", "brand_name", "model_name", "os", "popularity", "best_price",  "sellers_amount", "screen_size", "memory_size", "battery_size", "release_date"],
}

FUZZY_COLUMNS = {"model_name"}

def normalize_search(text):
    return text.strip().lower()

def validate_table(table):
    if table not in ALLOWED_SCHEMA:
        raise ValueError(f"INVALID TABLE '{table}'. Allowed tables: {list(ALLOWED_SCHEMA.keys())}")

def validate_column(table, col):
    if col == "*" or "(" in col:  
        # allow aggregates like COUNT(*), SUM(price)
        return True
    if col not in ALLOWED_SCHEMA[table]:
        raise ValueError(f"INVALID COLUMN '{col}' for table '{table}'. Allowed columns: {ALLOWED_SCHEMA[table]}")
    return True
