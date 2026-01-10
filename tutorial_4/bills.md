## Application 1: Indian Railways Ticket Booking System

### What You'll Learn
- Conditional statements with multiple conditions
- Price calculations based on different criteria
- User input validation
- Working with different data types

### Problem Statement
Create a simple ticket booking system for Indian Railways that calculates fare based on distance, class of travel, and passenger age.

### Requirements
- Ask user for passenger name, age, distance (in km), and class (Sleeper/AC/First Class)
- Base fare: Rs. 0.50 per km for Sleeper class
- AC class costs 2x of Sleeper, First Class costs 3x of Sleeper
- Senior citizens (age 60+) get 40% discount
- Children (age below 5) travel free
- Children (age 5-12) get 50% discount
- Display final ticket price with all details

### Sample Code Structure
```python
# Indian Railways Ticket Booking

print("=" * 50)
print("INDIAN RAILWAYS - TICKET BOOKING SYSTEM")
print("=" * 50)

# Input from user
passenger_name = input("Enter passenger name: ")
age = int(input("Enter age: "))
distance = float(input("Enter distance in km: "))
travel_class = input("Enter class (Sleeper/AC/First): ").lower()

# Base fare calculation
base_fare_per_km = 0.50
base_fare = distance * base_fare_per_km

# Class multiplier
if travel_class == "sleeper":
    class_multiplier = 1
    class_name = "Sleeper"
elif travel_class == "ac":
    class_multiplier = 2
    class_name = "AC"
elif travel_class == "first":
    class_multiplier = 3
    class_name = "First Class"
else:
    print("Invalid class selected!")
    class_multiplier = 1
    class_name = "Sleeper (Default)"

# Calculate fare with class
fare = base_fare * class_multiplier

# Age-based discount
if age < 5:
    discount = 100
    final_fare = 0
elif age >= 5 and age <= 12:
    discount = 50
    final_fare = fare * 0.5
elif age >= 60:
    discount = 40
    final_fare = fare * 0.6
else:
    discount = 0
    final_fare = fare

# Display ticket
print("\n" + "=" * 50)
print("TICKET DETAILS")
print("=" * 50)
print(f"Passenger Name: {passenger_name}")
print(f"Age: {age} years")
print(f"Distance: {distance} km")
print(f"Travel Class: {class_name}")
print(f"Base Fare: Rs. {fare:.2f}")
print(f"Discount Applied: {discount}%")
print(f"Final Fare: Rs. {final_fare:.2f}")
print("=" * 50)
print("Thank you for booking with Indian Railways!")
```

### Practice Task
Modify the program to:
- Add a category for students (age 13-25) with 25% discount
- Include a Tatkal booking option that adds 30% to the fare
- Ask for source and destination stations and display them
