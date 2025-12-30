print("======== Welcome to my shop ========")
print("============= Our menu =============")
print("")

samosa_price = 15
tea_price = 10
burger_price = 25


print("1. Samosa\t- Rs",samosa_price)
print("2. Tea\t\t- Rs",tea_price)
print("3. Burger\t- Rs",burger_price)
print("")

# samosa_quantity = 5
# print("Enter samosa quantity:",samosa_price)
# tea_quantity = 3
# print("Enter tea quantity:",tea_quantity)
# burger_quantity = 1
# print("Enter burger quantity:",burger_quantity)
# print("")

samosa_quantity = int(input("Enter samosa quantity: "))
tea_quantity = int(input("Enter tea quantity: "))
burger_quantity = int(input("Enter burger quantity: "))
print("")

samosa_bill = samosa_price * samosa_quantity
tea_bill = tea_price * tea_quantity
burger_bill = burger_price * burger_quantity

print("Item\tQuantity\tPrice\tTotal")
print("---------------------------------------")
print("Samosa\t",samosa_quantity,"\t\tRs ",samosa_price,"\tRs ",samosa_bill)
print("Tea\t",tea_quantity,"\t\tRs ",tea_price,"\tRs ",tea_bill)
print("Burger\t",burger_quantity,"\t\tRs ",burger_price,"\tRs ",burger_bill)
print("---------------------------------------")
print("")

total_bill = samosa_bill + tea_bill + burger_bill
print("Total bill:", total_bill)
