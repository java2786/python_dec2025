def add(a,b):
    print(a+b)
    
def mul(a,b):
    print(a*b)
    
add(4,8)


def getSamosa(price):
    if price == 15:
        return "aalo samosa"
    elif price == 25:
        return "paneer samosa"
    elif price == 50:
        return "pizza samosa"
    else:
        return None
    
print(getSamosa(15))

print(getSamosa(20))

print(getSamosa(25))

