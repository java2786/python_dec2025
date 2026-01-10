# valid right angle triangle

side_1 = int(input("Enter side 1: ")) # 5
side_2 = int(input("Enter side 2: ")) # 5
side_3 = int(input("Enter side 3: ")) # 5
h = 0 
p = 0 
b = 0 

if(side_1 > side_2 and side_1 > side_3):
    h = side_1
    b = side_2
    p = side_3
elif(side_2>side_1 and side_2 > side_3):
    h = side_2
    b = side_1
    p = side_3
elif(side_3>side_2 and side_3>side_1):
    h = side_3
    p = side_1
    b = side_2
else:
    print("Not right angle triangle")
    exit()
    
print(h)
print(b)
print(p)
if(h*h == p*p + b*b):
    print("Valid right angle triangle")
else:
    print("Not right angle triangle")
