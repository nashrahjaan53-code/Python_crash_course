# write a python program to translate a msg into secret code language.. use the rules below to translate normal English into secret code language

import random
import string
choice = input("Do you want to code or decode? ").lower()
message = input("Enter your message:  ")
if choice == "code":
    words = message.split()
    result = []
    for word in words:
        if len(word) < 3:
            result.append(word[::-1])
        else:
            start = " ".join(random.choices(string.ascii_lowercase, k =3))
            end = " ".join(random.choices(string.ascii_lowercase, k = 3))
            secret = start + word[1:] + word[0] + end
            result.append(secret)

    print("Secret message: ")
    print(" ".join(result))
elif choice == "decode":
    words = message.split()
    result = []
    for word in words:
        if len(word) < 3:
            result.append(word[::-1])
        else:
            middle = word[3:-3]
            original = middle[-1] + middle[:-1]
            result.append(original)
    print("Original message: ")
    print(" ".join(result))

else:
    print("Invalid choice")

            
