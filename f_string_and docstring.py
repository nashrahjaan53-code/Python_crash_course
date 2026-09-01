## F-string:
letter = "Hey my name is {1} and I am from {0}"
country = "Kashmir"
name = "Nashrah"
print(letter.format(country, name))
print(f"Hey my name is {name} and I am from{country}")
txt = "For only{price: .2f} dollars"
print(txt.format(price = 49.09999))
## if we want to print it as it is then:
print(f"We use f-strings like this: Hey my name is {{name}} and I am from{{country}}")


##important for interview:PEP8, Docstring:- Helps to understand an fun, method class or module:
def square(n):
    ''' Takes in a number n, returns the square of n '''
    print(n ** 2)
square(5)
print(square.__doc__)
    
##PEP 8: PYTHON ENHANCEMENT PROPOSAL:
###ZEN OF  PYTHON
