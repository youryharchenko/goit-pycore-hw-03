from  datetime  import datetime

def get_days_from_today(date: str):
    try:
        # Перетворюємо рядок на об'єкт datetime та беремо з нього тільки дату
        input_date = datetime.fromisoformat(date).date()
    except ValueError:
        # Помилка при перетворенні рядка в дату
        print(f"Рядок '{date}' містить некоректну дату або формат")
        days = None
    else:
        # Визначаємо поточеу дату
        current_date = datetime.now().date()
        # Визначаємо кількість днів між датами
        days = (current_date - input_date).days
    return days

if __name__ == "__main__":
    print(get_days_from_today('2025-05-01'))
    print(get_days_from_today('2025-01-01'))
    print(get_days_from_today('2026-01-01'))
    print(get_days_from_today('2026-1'))