nums = [i for i in range(5)]
print(nums)
##tuples:
t = tuple(i for i in range(5))
print(t)
##sets:
s = {i for i in range(5)}
print(s)
##dicts:
d = {i: i**2 for i in range(5)}
print(d)
names = ["chinko", "bolu", "molu"]
d = {name: len(name) for name in names}
print(d)
##list with conditions:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
##set with conditions:
even_squares_set = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares_set)
##dict with conditions:
even_squares_dict = {x: x**2 for x in range(10) if
    x % 2 == 0}
print(even_squares_dict)