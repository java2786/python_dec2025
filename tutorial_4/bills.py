# Ask user for passenger name, age, distance (in km), and class (Sleeper/AC/First Class)
# - Base fare: Rs. 0.50 per km for Sleeper class

name = input("Enter your name: ") # "Ramesh"
age = int(input("Enter your age: ")) # "45" -> 45
distance = int(input("Enter your distance (Km): ")) # "150" -> 150
category = input("Enter your class(Sleeper/AC/FirstClass): ") # "Ramesh"

# name = "Ramesh"
# age = 78
# distance = 150
# category = "AC"

base_fare = 0.50
fare = distance * base_fare

# print(type(name))
# print(type(age))
# print(type(base_fare))

if category!="Sleeper" and category!="AC" and category!="FirstClass":
    print("Invalid category")
else:
    print("Passenger name:",name)
    print("Passenger age:",age)
    print("Total distance:",distance)
    if(category=="Sleeper"):
        print("Total fare (Sleeper):",fare)
    elif(category=="AC"):
        fare = fare*2
        print("Total fare (AC):",fare)
    else:
        fare = fare*3
        print("Total fare (FirstClass):",fare)
        
    if(age>=60):
        fare = fare*.6
    elif(age<5):
        fare = 0
    elif(age>=5 and age<=12):
        fare = fare / 2

    print("Final amount:",fare)
