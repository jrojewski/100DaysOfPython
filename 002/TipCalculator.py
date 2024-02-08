print("---TIP CALCULATOR---")

bill = float(input("What was the total bill?\n"))
percentageTip = int(input("What percentage tip would you like to give?\n")) / 100
numOfPeople = float(input("How many people to split the bill?\n"))

calculatedShare = ((bill) / numOfPeople) * (1.0 + percentageTip)

print(f"Each person should pay: ${round(calculatedShare, 2)}")
