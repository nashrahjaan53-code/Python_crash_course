#a = int(input("enter ur age"))
#print("ur age is: ", a)
##conditional operators: >, <, >=, <=, ==, !=
#print(a <= 18)
#print(a >=18)
#print (a == 18)
#print(a != 18)
#if (a>18):
  #  print("u can drive")
#else:
 #   print("u cant drive")

#applePrice = 210
#budget = 200
#if(applePrice <= budget):
 #   print("Alexa, add 1kg apples to the cart")
#else:
    #print("alexa, dont add Apples in the cart")
          
##elif:
#num = int(input("Enter Any Value: "))
#if(num < 0):
 #   print("Number is negative")
#elif(num == 0):
 #   print("Number Is Zero")
#elif(num == 999):
 #   print("This is a Special number")
#else:
 #   print("Number is positive")
#print("I Am Happy Now")

##nested-ifelse:
#num = int(input("Enter Any Number: "))
#if (num < 0):
 #   print("Number is negative")
#elif(num > 0):
    #if(num <= 10):
     #   print("Number is between 0 - 10")
    #elif(num > 10 and num <= 20):
   #     print("Number between 10 -20")
  #  else:
 #       print("Number is greater than 20")
#else:
  #  print("Number is zero")

##EXERCISE the below one is how i did it but i did not mention hour and min and sec 
#import time
#time = int(input("Enter your time"))
#if(time < 12):
 #   print("Good Morning")
#elif(time > 12 and time < 1):
 #   print("Good AfterNoon")
#elif(time > 2):
 #   print("Good Evening")
#else:
   # print("enter proper time")
#import time
#timestamp = time.strftime('%H: %M: %S')
#print(timestamp)
#timestamp =int(time.strftime('%H'))
#print(timestamp)
#timestamp =int(time.strftime('%M'))
#print(timestamp)
#timestamp = int(time.strftime('%S'))
#print(timestamp)
#if(timestamp <= 0 and timestamp >= 12):
 #   print("Good Morning")
#elif(timestamp >= 12 and timestamp < 17):
 #   print("Good Afternoon")
#elif(timestamp >= 17 and timestamp !=19):
 #   print("Good Evening")
#else:
    #print("Good Night")

#Match case statements:
#x = int(input("Enter The Value Of X: "))
#match x:
    #case 0:
     #   print("x is zero")
    #case 4:
      #  print("case is 4")
    #case _ if x < 10:
     #   print("x is < 10")
    #case _:
      #  print(x)
        



    
