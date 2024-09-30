import datetime

def get_days_from_today(date: str) -> int | str:
    year, month, day = date.strip().split('-' if '-' in date else '/')
    try:
        return (datetime.datetime(int(year), int(month), int(day)) - datetime.datetime.now()).days
    except ValueError:
        return 'Wrong Info'

test_cases = [
    "2025-12-31",
    "2023-01-01",
    "2023-02-29",
    "2023-13-01",
    "2023-12-32",
    "2023/12/31",
    "abcd-12-31",
    "2023-ab-31",
    "2023-12-ab",
    " 2023-12-31 ",
]

for case in test_cases:
    print(get_days_from_today(case))