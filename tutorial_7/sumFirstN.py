# Print sum of first N natural numbers.

import time 

num = 10
sum = 0
# count = 1

# while count<=num:
#     sum = count + sum 
#     print("Count is",count,", Sum is",sum)
#     count = count + 1
#     time.sleep(4)
    
for count in range(1, num+1):
    sum = count + sum 
    print("Count is",count,", Sum is",sum)
    # time.sleep(4)
