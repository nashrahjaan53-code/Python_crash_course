#CREATE A LIST MAKE 3FUNCTIONS EVEN ODD AND SUM:
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
def odd_numbers(numbers):
    odds = []
    for num in numbers:
        if num % 2 != 0:
            odds.append(num)
    return odds
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
