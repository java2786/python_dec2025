# print 3 digit number in reverse order

num = 532

print(num%10, end="") # ld -> 2
num = num // 10 # last digit removed => 53

print(num%10, end="") # ld -> 3
num = num // 10 # last digit removed => 5

print(num%10) # ld -> 5
num = num // 10 # last digit removed => 0


# 235

""" 
num / 10 => decimal
num // 10 => quotient => make number smaller by removing last digit
num % 10 => remainder => gives last digit
"""