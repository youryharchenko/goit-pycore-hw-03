import re

def normalize_phone(phone_number: str):
    # Видаляємо все крім цифр та + 
    norm_phone = re.sub(r"[^\d\+]", "", phone_number)
    # Паттерн для рядка, що починається з +380
    pattern_plus_380 = r"^\+380(\d{2})(\d{7})$"
    # Паттерн для рядка, що починається з 380
    pattern_380 = r"^380(\d{2})(\d{7})$"
    # Паттерн для всіх інших варіантів
    pattern = r"^(\d{2,3})(\d{7})$"
    # Паттерн для складання нормалізованого номера
    replacement = r"+380\1\2"
    # Перевіряємо та нормалізуємо
    if re.search(pattern_plus_380, norm_phone): 
        norm_phone = re.sub(pattern_plus_380, replacement, norm_phone)
    elif re.search(pattern_380, norm_phone):
        norm_phone = re.sub(pattern_380, replacement, norm_phone)
    elif re.search(pattern, norm_phone):
        norm_phone = re.sub(pattern, replacement, norm_phone)
    else:
        norm_phone = f"Bad number: {phone_number}"

    return norm_phone

if __name__ == "__main__":
    test = [
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "1124",
    "+38(050)123-32-346",
    ]

    print([normalize_phone(p) for p in test])

    raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    ]

    print([normalize_phone(p) for p in raw_numbers])