print("Display Grade based on Number:")

Number = int(input("Enter your num: "))

if Number >= 90 and Number <= 100:
    print("Your Grade is A")
elif Number >= 80 and Number <= 89:
    print("Your Grade is B")
elif Number >= 70 and Number <= 79:
    print("Your Grade is C")
elif Number >= 60 and Number <= 69:
    print("Your Grade is D")
else:
    print("Fail or Invalid Input")
