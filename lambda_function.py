## LAMBDA FUN: is a small anonymous fun without a name

#def double(x):
 #   return x *2

#def appl(fx, value):
 #   return 6 + fx(value)

#double = lambda x: x*2
#cube = lambda x: x*x*x
#avg =  lambda x, y, z:(x + y +z) / 3
#print(double(5))
#print(cube(5))
#print(avg(3, 5, 10))
#print(appl(lambda x: x * x * x, 2))

##map, filter and reduce:

## map:
#def cube(x):
    #return x*x*x
#print(cube, 2)

#l =[1,2,4,6,7,5,4]
#newl = list(map(lambda x: x* x*x,l))
#print(newl)

##filter:

#def filter_function(a):
 #   return a>4
#newnewl = list(filter(filter_function, l))
#print(newnewl)

## reduce:
from functools import reduce
numbers = [1, 2, 3,4, 5] ## list of numbers
def mysum(x, y): ## calculate the sum of the numbers using the reduce fun
    return x + y
sum = reduce(mysum, numbers)

print(sum)


