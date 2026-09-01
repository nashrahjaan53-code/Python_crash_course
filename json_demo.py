import json

# data = {
#     "name": "Alice",
#     "age": 22,
#     "is_student": True,
#     "skills": ["Python", "React", "SQL"]
# }

# json_string = json.dumps(data,indent=4)
# print(json_string)

# json_string = '{"name": "Bob", "age": 25, "city": "Delhi"}'

# python_obj = json.loads(json_string)

# print(python_obj['name'])
# print(type(python_obj))


# data = {
#     "company": "Siffrum",
#     "employees": 50,
#     "remote": True
# }

# with open("company.json", "w") as file:
#     json.dump(data, file, indent=4)


with open("company.json", "r") as file:
    data = json.load(file)

print(data)
print(data["company"])

