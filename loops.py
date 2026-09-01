##for loop:
#name ='Chinko'
#for i in name:
    #print(i)
#colours = ["Red", "Blue", "Green","Yellow"]
#for colour in colours:
    #print(colour)
    #for i in colour:
      #  print(i)
##RANGE FUNC():
#for k in range(5):
 #   print(k + 1)
#for k in range(1, 2000):
   # print(k)
#for k in range(1, 12, 3):
  #  print(k)


##While loops:
#i = int(input("Enter the number : "))
#while(i <=39):
    #i = int(input("Enter the number : "))
   # print(i)
#print("Done with the loop")

#count = 5
#while(count > 0):
  #  print(count)
 #   count =  count - 1
#else:
    #print("I am inside else")

##BREAK AND CONTINUE:
#for i in range(12):
   # print("5 X", i + 1, "=", 5 * (i+ 1))
  #  if(i == 10):
 #       break
#print("Loop ko chod kar nikal gaya")

#for i in range(12):
    #if(i == 10):
      #  print("Skip the iteration")
     #   continue
    #print(" 5 X", i, "=", 5 * i)
## do while loop emulate:
i = 0
while True:
    print(i)
    i = i + 1
    if(i %100 == 0):
        break
    
