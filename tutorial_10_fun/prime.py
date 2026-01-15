def is_prime(n):
    flag = True
    for i in range(2,n):
        # print(f"dividing {n} by {i}")
        if n%i==0:
            flag = False
            break
    return flag



for i in range(2, 51):
    if is_prime(i)==True:
        print(f"{i} is prime number.")
