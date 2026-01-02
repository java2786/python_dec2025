# reverse 3 digit number and store in a variable

num = 532
res = 0

ld = num%10 # 2
num = num // 10 # last digit removed => 53
res = (res * 10) + ld # 2

ld = num%10 # 3
num = num // 10 # last digit removed => 5
res = (res * 10) + ld # 23

ld = num%10 # 5
num = num // 10 # last digit removed => 0
res = (res * 10) + ld # 235

print(res)

# output = 235

""" 
num / 10 => decimal
num // 10 => quotient => make number smaller by removing last digit
num % 10 => remainder => gives last digit
"""