num = 999 		# 0
copy = num        # 999
res = 0			# 176

ld = num%10 			# 1
num = num // 10 		# 67
res = (res * 10) + ld 	# 1

ld = num%10 			# 7
num = num // 10 		# 6
res = (res * 10) + ld 	# 17

ld = num%10 			# 6
num = num // 10 		# 0
res = (res * 10) + ld 	# 176


print(res)

print("Original: ",copy)
print("Reverse: ",res)

if(copy == res):
    print("same")
else:
    print("Not same")
