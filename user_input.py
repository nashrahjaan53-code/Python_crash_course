#a = input("enter ur name: ")
#print("my name is  ", a)
#x = input("enter one number : ")
#y = input("enter second number : ")
#print(x + y)
#print(x - y)
#print(x*y)
#print(x / y)
#print(x % ys)
#print(int(x) + int(y))
#print(int(x) - int(y))
#print(int(x) * int(y))
#print(int(x) / int(y))
#print(int(x) % int(y))

## string in python:
#name = "nashrah"
##indexing:
#print(name[0])
#print(name[1])
#friend = 'chinko'
#print("hello, " + name)
## triple quotes can be used to leave a lot of dist and write something in next line
#apple = '''he said,
#hii nashrah
#hey i am good
#"i want to eat an apple'''
#for character in name:
 #   print (character)
#for character in apple:
    #print(character)
#print(apple)
 ##string slicing:
#names = "nashrah, khan"
#print = (names[0: 6])
#fruit = "mango"
#len1 = len(fruit)
#print("mango is a ", len1, "letter word .")
#mangoLen = len(fruit)
#print(mangoLen)
#print(fruit[1:4])
#print(fruit[:])
#print(fruit[0 : -3])
#print(fruit[-1:len(fruit) -3])## this wont print anything
#print(fruit[-3:-1])
##quick quiz:
#nm = "Harry"
#print(nm[-4: -2])
 ##string methods:
a = "!!!!!Nashrah!!!!!!!!!!!!!! Nashrah"## strings are immutable
#print(len(a))
#print(a.upper())
#print(a.lower())
#print(a.rstrip("!"))
#print(a.replace("Nashrah!!!!!!!!!!!!!!!!!!!!!!" ,  "chinko"))
#print(a.split(" "))
blogHeading = "introduction tO js"
print(blogHeading.capitalize())## pehle word for captial krta hai
str1 = "WELCOME  to  THE CONSOLE !!! "
print(len(str1))
print(len(str1.center(50)))
print(a. count("Nashrah"))
print(str1.endswith("to" , 4, 10))
#print(str1.find("tott"))
#print(str1.index("THEEEE"))
str2 = "Heytherehowareyou"
print(str2.isalnum())
##str3 = "chinkoisaniceperson24"## if we remove the number it will be true
str3 = "chinkoisaniceperson"
print(str3.isalpha())
str21 = "we are doing not so great  but good \n"
print(str21)
print(str21.isprintable())
strempty= "             "
print(strempty.isspace())
streveryfirstcaptial= "Welcome To The World"
print(streveryfirstcaptial.istitle())## checks if all first letter is captial
print(streveryfirstcaptial.startswith("Welcome"))
str4 = "python is an interpreted language"
print(str4.swapcase())## uper ko lower lower ko uper
print(str4.title())## har ek pehle word ko captial krta hai
