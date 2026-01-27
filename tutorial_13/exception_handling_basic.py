a = 10
b = 0
print("Starting")

try:
    print(f"{a//b}")
    print("division is done")
except ZeroDivisionError:
    print("Not possible")
print("Ending")