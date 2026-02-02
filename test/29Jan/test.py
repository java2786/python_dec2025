""" 
. Palindrome or Not Palindrome
. Number of vowels
. Title case version of the string
"""

# Way 1
# str = "nitin"
# reversed_str = str[::-1]
# if str == reversed_str:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Way 2
str = "mom"
reversed_str = ""
v_count = 0

for i in range(len(str)):
    char = str[i]
    reversed_str =  char + reversed_str
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        v_count = v_count + 1
    
if str == reversed_str:
    print("Palindrome")
else:
    print("Not palindrome")
    
print(v_count)
    