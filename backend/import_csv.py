import csv
from db import SessionLocal
from models import PhoneDetail

def to_int(value):
    return int(value) if value not in ("", None) else None

def to_float(value):
    return float(value) if value not in ("", None) else None

def import_csv():
    session = SessionLocal()

    with open("backend/data/phones.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            phone = PhoneDetail(
                brand_name=row["brand_name"],
                model_name=row["model_name"],
                os=row["os"],
                popularity=to_int(row["popularity"]),
                best_price=to_float(row["best_price"]),
                lowest_price=to_float(row["lowest_price"]),
                highest_price=to_float(row["highest_price"]),
                sellers_amount=to_int(row["sellers_amount"]),
                screen_size=to_float(row["screen_size"]),
                memory_size=to_float(row["memory_size"]),
                battery_size=to_float(row["battery_size"]),
                release_date=row["release_date"],
            )
            session.add(phone)

        session.commit()
        session.close()

if __name__ == "__main__":
    import_csv()
