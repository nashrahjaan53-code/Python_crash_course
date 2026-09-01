##exception_handling
#a = input("Enter the number: ")
#print(f"Multiplication table of {a} is :")

#try:
  #  for i in range(1, 11):
 #       print(f"{int(a)} X {i} = {int(a) * i }")
#except:
   # print("Sorry some error occured")
#print("Some lines of code")
#print("End of Program")

#try:
    #num = int(input("Enter an integer:  "))
    #a = [6, 3]
 #   print(a[num])
#except ValueError:
    #print("Number entered is not an integer. ")
              
##Finally:
#def func1():
 #   try:
  #      l = [1, 5, 6, 7]
   #     i = int(input("Enter the index: "))
    #    print(i)
     #   return 1
    #except:
      #  print("Some error occured")
       # return 0

    #finally:
     #   print("I am always executed")

#x = func1()
#print(x)


##Raising Custom Errors:
a = int(input("enter any  value between 5 and 9: "))
if( a < 5 or a >9):
    raise ValueError("Value should be between 5 and 9")
else:
    print("Quit")
    
