import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    try:
        min, max, quantity = int(min), int(max), int(quantity)
    except (ValueError, TypeError):
        return []
    if min < 1 or max > 1000 or(min > quantity > max):
        return []
    try:
        return sorted(random.sample(range(min, max), quantity))
    except (ValueError, TypeError):
        return []

test_cases = [
    (1, 49, 6),
    (1, 10, 5),
    (1, 1000000, 10),
    (50, 60, 3),
    (1, 50, 50),
    (1, 50, 51),
    (50, 1, 5),
    (1, 50, 0),
    (1, 50, -5),
    ('1', '50', '5'),
    (1.5, 50.5, 5),
    ('a', 'b', 'c'),
    (None, None, None),
]

for case in test_cases:
    min, max, quantity = case
    print(get_numbers_ticket(min, max, quantity))