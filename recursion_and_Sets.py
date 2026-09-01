#factorial(7) = 7* 6* 5 *3 * 2* 1
#def factorial(n):
   # if(n == 0 or n == 1):
  #      return 1
 #   else:
 #       return n * factorial(n-1)
#print(factorial(3))
#print(factorial(4))
#print(factorial(5))
#print(factorial(1))
## fibonacci sequence:
#def fibonacci(x):
   # if (x == 0 or x == 1):
   #     return 1
  #  else:
 #       return fibonacci(x-1) + fibonacci(x- 2)
#print(fibonacci(4))
#print(fibonacci(7))


##Set: they are unordered and dont repeat
s = {2, 4,2, 6}
print(s)
info = {"Carla", 19, False, 5.0,19}
s1 =set() ## if empty set type to print
print(type(s1))
for value in info:
    print(value)

## Methods of set:
#1.union: donu sets ko merge krkai result
s2 = {4,7,86,3,56}
s3 = {5,9,10}
print(s1.union(s2))
print(s2,s3)
s2.update(s3)
#INtersec and intersec update: gives value which is repeated
cities = {"Tokeyo2", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokeyo", "Seoul", "Kabul", "Madrid2"}
#cities.intersection(cities2)
print(cities)
## difference and difference update:
#cities3 = cities.difference(cities2)
#print(cities3)
## for manuplating the sets:
#isdisjoint
#print(cities.isdisjoint(cities2))

#issuperset() are they first present or not
print(cities.issuperset(cities2))

##issubset()
print(cities.issubset(cities2))

## add:
cities.add("Helsinki")
print(cities)

##remove or discard:
cities.remove("Tokeyo2")
print(cities)

##pop: removes any member
item = cities.pop()
print(cities)
print(item)

#del used to delete whole set
#clear deleted only some
