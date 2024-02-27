weight=int(input("Weight:"))
unit=input("lbs or kg:")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"You are {converted} kg.")
else:
    converted=weight/0.45
    print(f"You are {converted} lbs")     