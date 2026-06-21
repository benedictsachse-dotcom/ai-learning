bill=float(input("Total bill: "))
friends=int(input("How many friends: "))
tip=float(input("Tip percentage: "))

each_person = (bill + (bill * tip) / 100) / friends
print()
print("Each person pays:", each_person)
