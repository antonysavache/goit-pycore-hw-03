def normalize_phone(phone: str):
    normizied_phone = ''
    phone = phone.replace(' ', '')

    for value in phone:
        if value.isdigit():
            normizied_phone = normizied_phone + value

    if normizied_phone.startswith('38'):
        return '+' + normizied_phone
    else:
        return '+38' + normizied_phone

test_cases = [
    "+38(050)123-45-67",
    "050xxxxxxx",
    "38050123456",
    "(050)123-4567",
    "38050 123 45 67",
    "+38050123456",
    "8050123456",
    "7050123456",
    "050123456",
    "80501234567",
    "12345",
    "",
    "abcdefg",
    "+38(050)123-45-67 123",
    "38",
    "+",
    "380",
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

for case in test_cases:
    print(normalize_phone(case))