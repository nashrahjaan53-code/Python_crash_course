
def ascii_sunrise():
    import os
    import time
    frames = []
    for i in range(10):
        sun_position = 20 - i * 2  
        if i < 5:
            sky = "🌅" * 5  
        else:
            sky = "☀️" * 5 
    
        frame = f"""
        {' ' * 30}{sky}
        {' ' * 30}{'🌳' * 5}
        
        {' ' * sun_position}{'🌞'}
        
        {' ' * 30}{'🌲' * 5}
        {'═' * 60}
        Time: {i+6}:00 AM
        """
        frames.append(frame)
    
  
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(1)
ascii_sunrise()







import math
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n
for i in range(1, 10000):
    if is_perfect_number(i):
        print(f"Perfect number found: {i}")


        import calendar
from datetime import datetime, timedelta
cal = calendar.month(2026, 1)          
month_days = calendar.monthrange(2026, 1)  
is_leap = calendar.isleap(2026)         
day_name = calendar.day_name[0]           
month_name = calendar.month_name[1]     
def business_days_between(start_date, end_date):
    """Calculate business days between two dates"""
    return np.busday_count(start_date.date(), end_date.date())
