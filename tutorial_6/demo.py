# Find if given number is Palindrome

num = 1991 		
copy = num        
res = 0			

while num>0:
    ld = num%10 			
    num = num // 10 		
    res = (res * 10) + ld 	

if(copy == res):
    print(copy,"Palindrome")
else:
    print(copy,"Not Palindrome")
