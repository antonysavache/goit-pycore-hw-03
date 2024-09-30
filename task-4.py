from datetime import datetime, date, timedelta

users = [
    {"name": "John Smith", "birthday": "1985.10.02"},
    {"name": "Emily Johnson", "birthday": "1990.10.05"},
    {"name": "Michael Brown", "birthday": "1988.09.30"},
    {"name": "Jessica Davis", "birthday": "1992.10.07"},
    {"name": "Christopher Wilson", "birthday": "1983.09.28"},
    {"name": "Ashley Martinez", "birthday": "1995.10.01"},
    {"name": "Matthew Taylor", "birthday": "1980.10.06"},
    {"name": "Amanda Anderson", "birthday": "1998.10.08"},
    {"name": "David Thomas", "birthday": "1987.02.29"},
    {"name": "Jennifer Jackson", "birthday": "1993.12.31"},
]

weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
weekends = ['Saturday', 'Sunday']
SHIFT = 7

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = date.today()
    today_plus_7_days = today + timedelta(days=SHIFT)

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if today <= birthday_this_year <= today_plus_7_days:
                congratulation_date = birthday_this_year

                if weekdays[congratulation_date.weekday()] in weekends:
                    days_ahead = 7 - congratulation_date.weekday()
                    congratulation_date += timedelta(days=days_ahead)

                upcoming_birthdays.append({
                    'name': user['name'],
                    'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
                })
        except ValueError:
            continue

    return upcoming_birthdays

print(get_upcoming_birthdays(users))