# squares = []
# for x in range(1, 6):
#     squares.append(x**2)
# print(squares)


# squares = [x**2 for x in range(1, 6)]
# print(squares)

# nums = [1, 2, 3, 4, 5, 6]
# evens = [n for n in nums if n % 2 == 0]
# print(evens)

# inputs = ["apple", "", "banana", "", "grape"]
# cleaned = [item for item in inputs if item]
# print(cleaned)

# users = [
#     {"id": 1, "username": "laila"},
#     {"id": 2, "username": "arjun"},
#     {"id": 3, "username": "neha"}
# ]

# usernames = [user["username"] for user in users]
# print(usernames)

# labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
# print(labels)
# names = ["laila", "meer", "python"]
# upper_names = [name.upper() for name in names]
# print(upper_names)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)
