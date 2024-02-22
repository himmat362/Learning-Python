credit=bool(input("Enter T for good credit otherwise press enter\n"))
#for boolean input, any value is considered true and no value is considered false
price=1000000
if credit:
    print("Good Credit:Put down $",((10/100)*price))
else:
    print("Not Good Credit:Put down $",((20/100)*price))