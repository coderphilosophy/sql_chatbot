from backend.execution.validator import *

def run_intent(db, intent):
    """
    Execute validated intent using SQLAlchemy ORM (db.query)
    """
    # Basic validation
    table = intent.get("table")
    columns = intent.get("columns")

    if not table or not columns:
        raise ValueError("Intent must include table and columns")

    validate_table(table)

    model = MODEL_MAP[table]

    # Validate requested columns
    for col in columns:
        validate_column(table, col)

    # Start ORM query
    query = db.query(model)

    #    filters
    for f in intent.get("filters", []):
        col_name = f["column"]
        op = f.get("op", "=")
        value = f["value"]
        validate_column(table, col_name)

        orm_col = getattr(model, col_name)

        if col_name in FUZZY_COLUMNS:
            query = query.filter(orm_col.ilike(f"%{value}%"))
        elif op == "=":
            query = query.filter(orm_col == value)
        elif op == "<":
            query = query.filter(orm_col < value)
        elif op == "<=":
            query = query.filter(orm_col <= value)
        elif op == ">":
            query = query.filter(orm_col > value)
        elif op == ">=":
            query = query.filter(orm_col >= value)
        elif op.lower() == "like":
            query = query.filter(orm_col.like(value))
        else:
            raise ValueError(f"Unsupported operator '{op}'")

    # ORDER BY
    if intent.get("order_by"):
        for order in intent["order_by"]:
            col_name = order["column"]
            direction = order.get("direction", "asc")

            validate_column(table, col_name)

            orm_col = getattr(model, col_name)

            if direction.lower() == "desc":
                query = query.order_by(orm_col.desc())
            else:
                query = query.order_by(orm_col.asc())

    
    # LIMIT
    if intent.get("limit"):
        query = query.limit(intent["limit"])

    # Execute
    print(query)
    results = query.all()

    print("\n=== ORM QUERY DEBUG ===")
    print("MODEL:", model.__name__)
    print("FILTERS:", intent.get("filters"))
    print("LIMIT:", intent.get("limit"))
    print("ROWS RETURNED:", len(results))
    print("=======================\n")

    for phone in results: 
        print(phone.brand_name, phone.model_name, phone.best_price)

    return results

# result = run_intent(db, {'action': 'select',
#  'table': 'phone_details',
#  'columns': ['brand_name',
#   'model_name',
#   'best_price',
#   'os',
#   'popularity',
#   'sellers_amount',
#   'screen_size',
#   'memory_size',
#   'battery_size',
#   'release_date'],
#  'filters': [{'column': 'model_name',
#    'op': '=',
#    'value': 'A12 4/64GB Blue'}],
#  'group_by': [],
#  'join': None,
#  'limit': 1})

# for phone in result:
#     print(phone.brand_name, phone.model_name, phone.best_price)