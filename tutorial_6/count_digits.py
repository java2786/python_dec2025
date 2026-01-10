import time 
count = 0
num = 5832

while num>0:
    count = count + 1
    num = num // 10
    print("Num:",num,",Count:",count)
    time.sleep(2)



