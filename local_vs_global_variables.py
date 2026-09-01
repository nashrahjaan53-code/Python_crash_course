##local vs global variable

#x = 4
#print(x)

#def hello():
 #   x = 5
  #  print(x)
   # print("Hello Nashrah")


#print(f"The global x is {x}")
#hello()
#print(f"The global x is {x}")

x = 10 ## global variable
def my_function():
    global x   ## used when we have to overwrite an global var
    x = 4
    y = 5
    print(y)

#my_function()
#print(x)
#print(y)  ## this will cause an error becayse y is a local var and is not accesible outside of the fun
