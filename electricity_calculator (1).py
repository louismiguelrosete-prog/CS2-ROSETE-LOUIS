# Electricity Bill Calculator
RATE = 12.90

# 1. Customer name -- Must not be empty
while True:
    name = input("Enter customer name: ")
    
    if name.strip() != "":
        break
    else:
        print("Invalid name. Name must not be empty")

# 2. Previous reading -- Number at least 0
while True:
    previous = float(input("Enter previous meter reading: "))
    if previous >= 0:
        break
    else:
        print("Number must atleast be zero")
        

# 3. Current reading -- Number at least the previous reading
while True:
    current = float(input("Enter current meter reading: "))
    if current >= previous:
        break
    else:
        print("Current reading must be atleast previous reading")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
