import csv
from datetime import datetime
from pathlib import Path

BASE = Path("../dados")
ORDERS_CSV = BASE / "olist_orders_dataset.csv"
ITEMS_CSV = BASE / "olist_order_items_dataset.csv"
OUTPUT_CSV = BASE / "dim_time.csv"

ORDERS_DATE_COLS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]
ITEMS_DATE_COLS = ["shipping_limit_date"]

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def collect_dates(path: Path, columns: list[str], bucket: set) -> int:
    read = 0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            read += 1
            for col in columns:
                raw = (row.get(col) or "").strip()
                if len(raw) < 10:
                    continue
                try:
                    d = datetime.strptime(raw[:10], "%Y-%m-%d").date()
                    bucket.add(d)
                except ValueError:
                    pass
    return read


def main() -> None:
    dates: set = set()

    n_orders = collect_dates(ORDERS_CSV, ORDERS_DATE_COLS, dates)
    print(f"orders lidas:  {n_orders}")
    n_items = collect_dates(ITEMS_CSV, ITEMS_DATE_COLS, dates)
    print(f"items lidos:   {n_items}")

    rows = []
    for d in sorted(dates):
        rows.append({
            "datum_date": d.isoformat(),            # yyyy-MM-dd
            "time_day": d.day,
            "time_month": d.month,
            "time_year": d.year,
            "time_weekday": WEEKDAYS[d.weekday()],
            "time_quarter": f"Q{(d.month - 1) // 3 + 1}",
        })

    fields = ["datum_date", "time_day", "time_month",
              "time_year", "time_weekday", "time_quarter"]
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"datas unicas:  {len(rows)}")
    print(f"arquivo gerado: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
