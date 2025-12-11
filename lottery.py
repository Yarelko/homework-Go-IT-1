import random

def get_numbers_ticket(min_value, max_value, quantity):
    if (min_value < 1 or
        max_value > 1000 or
        min_value > max_value or
        quantity > (max_value - min_value + 1) or
        quantity <= 0):
        return []

    numbers = random.sample(range(min_value, max_value + 1), quantity)

    return sorted(numbers)
