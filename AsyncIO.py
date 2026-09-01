#import asyncio
#import time

#async def function1():
  #  await asyncio.sleep(1)
 #   print("func 1")
 
#async def function2():
  #  await asyncio.sleep(1)
 #   print("func 2")

#async def function3():
  #  await asyncio.sleep(2)
 #   print("func 3")

#async def main():
    #L = await asyncio.gather(
     #   function1(),
    #    function2(),
   #     function3()

  #  )
 #   print(L)
   
##task = asyncio.create_task(function1())
# await function1()
# await function2()
# await function3()

#asyncio.run(main())

import requests

# The official Instagram favicon URL
url = "https://instagram.com"
output_file = "instagram_favicon.ico"

# Add a User-Agent header so Instagram's server processes the request normally
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    print("Downloading Instagram favicon...")
    response = requests.get(url, headers=headers, timeout=10)
    
    # Check if the download was successful (HTTP status 200)
    response.raise_for_status()
    
    # Save the file in binary write mode ('wb')
    with open(output_file, "wb") as file:
        file.write(response.content)
        
    print(f"Success! Saved as '{output_file}'")

except requests.exceptions.RequestException as e:
    print(f"Failed to download icon. Error: {e}")

    
    
    
