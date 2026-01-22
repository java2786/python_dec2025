# item1 = name, price, quantity, total

# item1 = {"name": "Dosa", "price": 70, "quantity": 0, "total": 0}
# item2 = {"name": "Pizza", "price": 120, "quantity": 0, "total": 0}
# item3 = {"name": "Samosa", "price": 20, "quantity": 0, "total": 0}

items = [
    {"name": "Dosa", "price": 70, "quantity": 0, "total": 0},
    {"name": "Pizza", "price": 120, "quantity": 0, "total": 0},
    {"name": "Samosa", "price": 20, "quantity": 0, "total": 0},
    {"name": "Tea", "price": 10, "quantity": 0, "total": 0},
    {"name": "Pakora", "price": 50, "quantity": 0, "total": 0}
]

print("========Welcome to Sohan's Restaurant========")
print("==================Our menu===================")

for i in range(len(items)):
    print(f'{i+1}. {items[i]["name"]} - Rs {items[i]["price"]}/-')    
    
for i in range(len(items)):
    items[i]["quantity"] = int(input(f'{items[i]["name"]} Quantity: '))
    items[i]["total"] = items[i]["price"] * items[i]["quantity"]

    # print(items[i]["name"])
    # print(items[i]["price"])
print("\n\n===========Mohan's Bill=============")
final_bill = 0
for i in range(len(items)):
    print(f'{items[i]["name"]}: {items[i]["quantity"]}x Rs {items[i]["price"]} = {items[i]["total"]}')
    final_bill = final_bill + items[i]["total"]


print("--------------------------------------------------------------------")

print(f"Total bill: Rs {final_bill}")
