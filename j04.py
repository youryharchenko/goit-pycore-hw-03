from  datetime  import datetime, timedelta

def get_upcoming_birthdays(users):
    # Функція перевіряє чи дата потрапляє в потрібний інтервал дат
    def birthday_in_interval(user, today, n_day):
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        delta = (birthday - today).days 
        return delta < n_day and delta >= 0
    # Функція створює словник привітання (при потребі зсуває дату на понеділок)
    def make_congratulation_date(user):
        congratulation_date = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        if congratulation_date.weekday() > 4:
            congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))
        return {'name': user['name'], 'congratulation_date': congratulation_date.strftime("%Y.%m.%d")}

    today = datetime.now().date()
    # Формуємо список привітань на наступні 7 днів
    return [make_congratulation_date(user) for user in users if birthday_in_interval(user, today, 7)]

if __name__ == "__main__":

    test = [
    {'name': 'User 1', 'birthday': '2025.05.27'},
    {'name': 'User 2', 'birthday': '2025.05.28'},
    {'name': 'User 3', 'birthday': '2025.05.29'},
    {'name': 'User 4', 'birthday': '2025.05.30'},
    {'name': 'User 5', 'birthday': '2025.05.31'},
    {'name': 'User 6', 'birthday': '2025.06.01'},
    {'name': 'User 7', 'birthday': '2025.06.02'},
    {'name': 'User 8', 'birthday': '2025.06.03'},
    {'name': 'User 9', 'birthday': '2025.06.04'},
    {'name': 'User 10', 'birthday': '2025.06.05'},
    ]

    print(get_upcoming_birthdays(test))