# welcome to sohan's restaurant
# Our menu
# dosa - Rs 50
# idli - Rs 25
# colddrink - Rs 50
# dosa quantity:2
# idli quantity:2
# colddrink quantity:0

print("welcome to sohan's restaurant")
print("our menu")
dosa_price = 55
idli_price = 20
print("dosa - Rs",dosa_price)
print("idli - Rs",idli_price)

#taking quantity
dosa_quantity = 2
idli_quantity = 3
print("dosa quantity:",dosa_quantity)
print("idli quantity:",idli_quantity)

#adding bill
dosa_bill = dosa_price * dosa_quantity
idli_bill = idli_price * idli_quantity

print("Dosa Bill:",dosa_bill)
print("Idli bill:",idli_bill)

total_bill = dosa_bill + idli_bill

print("Total bill:",total_bill)