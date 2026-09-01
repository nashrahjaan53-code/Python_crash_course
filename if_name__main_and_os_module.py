#import welcoming
#welcoming.welcome()
## os module:
import os

# Create folders Day1 to Day100 safely
for i in range(100):
    os.makedirs(f'data/Day{i + 1}', exist_ok=True)

print('Folders created successfully')
