import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    # Перевіряємо взідні параметри
    if min < 1 or max > 1000 or quantity > max or quantity < min:
        print("Некоректні вхідні параметри")
        return []
    # Для унікальності використаємо множину (set)
    uniq = set()
    # Генеруємо в циклі випадкові числа поки не отримаємо потрібну кількість унікальних
    while len(uniq) < quantity:
        uniq.add(random.randint(min, max))
    # Перетворюємо множину на список, сортуємо та повертаємо
    return sorted(list(uniq))

if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))
    print(get_numbers_ticket(1, 36, 5))
    print(get_numbers_ticket(1, 36, 37))