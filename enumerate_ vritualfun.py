##enumerate function:
#marks = [12, 56, 32, 96, 12, 45,1, 4]
#for index, mark in enumerate(marks):
   # print(mark)
  #  if (index == 3):
 #       print("Nashrah, Rocks")
        
#fruits = ['apple', 'banana', 'mango']
#for index, fruit in enumerate(fruits, start =1):
   # print(index, fruit)
    
## virtual environment:
#python -m venv myenv ## creating the env
## for activating it:
#source myenv/bin/activate ## for mac and linux
## for windows:
#myenv\Scripts\activate.bat (#in powershell use ps1 instead of bat)
##The requiremnets.txt file:
#pip freeze > requirements.txt ## output the list of installed packages
#pip install -r requirements.txt ## install the packages in requirements file


## How import works in python
#import math
#result = math.floor(4.2341)
#print(result)

#from math import sqrt, pi
#result = sqrt(9) * pi
#print(result)

## The "AS" keyword:
import math as m
result = m.sqrt(9)
print(result)

## The dir func:
import math
print (dir(math)) ## can see all func and methods of the module
def welcome():
    print("Hey u are welcome my friend")

nashrah = "A good girl"
    

