##Dictionaries
dic = {
    "Nashrah": "Human Being",
    "Spoon" : "Object"

    }
#print(dic["Nashrah"])
info = {'name': 'Chinko', 'age': 3, 'eligible': True}
#print(info)
#print(info['name'])
# to print all keys:
#print(info.keys())
##to get all values
#print(info.values())
#for key in info.keys():
    #print(info[key])
print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
    
## dictionary methods:
ep1 = {122: 45, 123: 89, 124: 56, 234: 67}
ep2= {222: 67, 566: 90}
#ep1.update(ep2)
print(ep1)
## clear:
#ep1.clear()
#print(ep1)
#ep1.popitem()
print(ep1)
del ep1
print(ep1)



