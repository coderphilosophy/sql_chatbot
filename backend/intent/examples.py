FEW_EXAMPLES = [
    {
    "user": "What is the price of Samsung Galaxy S21?",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["best_price"],
        "filters": [
            {"column": "model_name", "op": "=", "value": "Samsung Galaxy S21"}
        ],
        "order_by": [],
        "group_by": [],
        "join": None,
        "limit": 1
        }
    },


    {
    "user": "List all phones by Samsung",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["model_name", "best_price"],
        "filters": [
            {"column": "brand_name", "op": "=", "value": "Samsung"}
        ],
        "order_by": [{"column": "best_price", "direction": "asc"}],
        "group_by": [],
        "join": None,
        "limit": None
    }
}
,

{
    "user": "Show phones under 20000",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["brand_name", "model_name", "best_price"],
        "filters": [
            {"column": "best_price", "op": "<=", "value": 20000}
        ],
        "order_by": [{"column": "best_price", "direction": "asc"}],
        "group_by": [],
        "join": None,
        "limit": None
    }
},

    # Example 4: Popular phones
    {
    "user": "Which are the most popular phones?",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["brand_name", "model_name", "popularity"],
        "filters": [],
        "order_by": [{"column": "popularity", "direction": "desc"}],
        "group_by": [],
        "join": None,
        "limit": 5
        }
    },
    
    # Example 5: Phone specifications
    {
        "user": "What is the battery size of iPhone 13?",
        "json": {
            "action": "select",
            "table": "phone_details",
            "columns": ["battery_size"],
            "filters": [
                {"column": "model_name", "op": "=", "value": "iPhone 13"}
            ],
            "group_by": [],
            "join": None,
            "limit": 1
        }
    },

    # Example 6: Cheapest phone
    {
    "user": "Which is the cheapest phone?",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["brand_name", "model_name", "best_price"],
        "filters": [],
        "order_by": [{"column": "best_price", "direction": "asc"}],
        "group_by": [],
        "join": None,
        "limit": 1
    }
},

    # Example 7: Phones by OS
    {
        "user": "List all Android phones",
        "json": {
            "action": "select",
            "table": "phone_details",
            "columns": ["brand_name", "model_name", "best_price"],
            "filters": [
                {"column": "os", "op": "=", "value": "Android"}
            ],
            "group_by": [],
            "join": None,
            "limit": None
        }
    },
    # Example 8: Phones in a price range
    {
    "user": "Phones between 30000 and 50000",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["brand_name", "model_name", "best_price"],
        "filters": [
            {"column": "best_price", "op": ">=", "value": 30000},
            {"column": "best_price", "op": "<=", "value": 50000}
        ],
        "order_by": [{"column": "best_price", "direction": "asc"}],
        "group_by": [],
        "join": None,
        "limit": None
    }
},
# Example 9: Count of phones per brand
{
    "user": "How many phones does each brand have?",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["brand_name", "COUNT(*)"],
        "filters": [],
        "order_by": [],
        "group_by": ["brand_name"],
        "join": None,
        "limit": None
    }
},
# Example 10: Average price per brand
{
    "user": "What is the average phone price for each brand?",
    "json": {
        "action": "select",
        "table": "phone_details",
        "columns": ["brand_name", "AVG(best_price)"],
        "filters": [],
        "order_by": [],
        "group_by": ["brand_name"],
        "join": None,
        "limit": None
    }
}
]