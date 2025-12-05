from datetime import datetime, timedelta

def date_to_string(date):
    return date.strftime("%d.%m.%Y")

def str_to_date(date_string):
    return datetime.strptime(date_string, "%d.%m.%Y")

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday