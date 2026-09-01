#requests module:
import requests
response = requests.get("https://www.google.com")
print(response.text)


url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1,
}
headers ={
    'Content-type': 'application/json; charset = UTF-8'
}

response = requests.post(url, headers = headers, json = data)
print(response.text)

## bs4:
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for heading in soup.find_all("h2"):
    print(heading.text)
