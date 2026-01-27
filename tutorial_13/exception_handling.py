# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

try:
    filename = "/Volumes/My Shared Files/shared/thispc_host/python_dec2025/tutorial_13/numbers.txt"
    with open(filename) as obj:
        lines = obj.readlines()
        nums = []
        for line in lines:
            nums.append(int(line))

    print(nums)
    a = nums[0]
    b = nums[1]
    # c = nums[2]
    print(f"Div: {a/b}")
except ValueError:
    print("Can not find digits") 
except ZeroDivisionError:
    print("Can not divide by zero")
except FileNotFoundError:
    print("File location is not correct") 
except IndexError:
    print("Enough numbers are not found in file")
