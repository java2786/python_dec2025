def purchase():
    name = input("Enter your name: ")

    item_name = input("Enter item to purchase: ")
    item_quantity = int(input("Enter item quantity to purchase: "))
    item_price = 100

    bill_amount = item_quantity * item_price
    if(bill_amount>500):
        bill_amount = bill_amount * .98
        

    print(f"Welcome {name}, you are purchasing {item_name} with  {item_quantity} quantity.")
    print(f"Your final bill amount is {bill_amount}.")



for i in range(1,1):
    print("Running for i",i)
    purchase() # calling function -> execute code which is inside function


