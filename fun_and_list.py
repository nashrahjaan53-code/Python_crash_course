##Functions:
#def calculateGmean(a,b):
 #   mean = (a*b)/(a + b)
  #  print (mean)
#def isGreater(a, b):
 #   if(a > b):
  #      print("First number is greater")
   # else:
    #    print("Second number is greater or equal")
#def isLesser(a, b):
 #  pass ## kuch krnai ki zarurat nhi hai 
#a = 9
#b = 8
#gmean1= (a*b)/(a + b)
#print(gmean1)
#calculateGmean(a, b)
#isGreater(a, b)
#c =8
#d= 7
#gmean2 =(c * d)/(c + d)
#print(gmean2)
#calculateGmean(c, d)
#isGreater(c,d)

##Func args and return statement:
 
def average(a = 9,b = 1):
    print("The average is ", (a+b)/2)
#average(4,6)
average(b =9)
##keyword args:
average(b = 9, a =21)
##default:
def name (fname, mname = "John", lname = "Whatson"):
    print("Hello", fname, mname, lname)
name("Amy", "Agarwal", "Jain")

## required args:
def name(fname, mname, lname):
    print("Hello", fname, mname, lname)

name("Chinko", "Shah","Ji")

##variable length args:
#def avg(*numbers):
    #print(type(numbers))
    #sum = 0
   # for i in numbers:
  #      sum = sum + i
    #print("Average is: ", sum / len(numbers))
    #return 7
 #   return sum / len(numbers)
#c = avg(5, 6, 7, 1)
#print(c)

##now lets take it as dict:
#def name(**name):
  #  print(type(name))
 #   print("Hello", name["fname"], name["mname"], name["lname"])
#name(mname = "Sarver", fname = "Nashrah", lname = "Khan")

 ##list
#marks= [3, 5, 6,"True", 7, 8, 9, 23, 34, 45, "Chinko"]
#print(marks)
#print(type(marks))
##list index:
#print(marks[0]) ##positive indexing
#print(marks[1])
#print(marks[2])
#print(marks[3])
#print(marks[-3]) ## negt index
#print(marks[len(marks) -3])## to make index of negt convert it into positivr
#print(marks[5-3])
#if "True" in marks:
 #   print("Yes")
#if "rue" in marks:
 #   print("Yes")
#print(marks[1:9])
#print(marks[1:9:3])
##List comprehension:
#lst= [i* i for i in range(10)]
#print([lst])
#lst = [i * i for i in range(10) if i%2 ==0]
#print(lst)

 ##list methods:
#l = [11,45,1,2,4,6,1, 1]
#print(l)
#l.append(7) ## adds item at the end
#l.sort()
#l.reverse ## orignial list ko change kr deta hai
#print (l.index(1))
#print(l.count(1))
#m = l.copy()
#m[0] = 0
#print(l)
#l.insert(1,899)
#print(l)
#m =[900, 1000,1100]
#k = l+ m 
#l.extend(m)
#print(k)
#print(l)
