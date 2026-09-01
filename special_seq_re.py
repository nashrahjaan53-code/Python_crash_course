import re

text = "Order 45 costs 1200"
print(re.findall(r"\d", text))
print(re.findall(r"\D", "A1B2"))
print(re.findall(r"\w", "hi_12!"))
print(re.findall(r"\W", "hi_12!"))
print(re.findall(r"\s", "hi there!"))
print(re.findall(r"\S", "hi there!"))
print(bool(re.search(r"\AHello", "Hello World")))
print(bool(re.search(r"\AWorld", "Hello World")))
print(bool(re.search(r"World\Z", "Hello World")))
print(re.findall(r"\bcat\b", "cat scatter cat"))
print(re.findall(r"\Bcat", "scatter cat"))
