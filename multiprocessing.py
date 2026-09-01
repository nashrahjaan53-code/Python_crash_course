##multiporcessing:
import multiprocessing
import requests

def downloadFile(url, name):
    response = requests.get(url)
    open(f"{name}.jpg",
    "wb").write(response.content)

url = "https://picsum.photos/2000/300"
pros = []
for i in range(5):
    #downloadFile(url, i)
    p = multiprocessing.Process(target= downloadFile, args = [url,i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]
    results = executor.map(downloadFile, l1, l2)
    for r in results:
        print(r)
    
    
