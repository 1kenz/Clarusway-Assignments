input1 = input("Are you a cigarette addict older than 75 years old? Yes or No: ").title().strip()
if input1 == "Yes":
    age = True
else:
    age = False

input2 = input("Do you have a severe chronic disease? Yes or No: ").title().strip()
if input2 == "Yes":
    chronic = True
else :
    chronic = False

input3 = input("Is your immune system too weak? Yes or No: ").title().strip()
if input3 == "Yes":
    immune = True
else: 
    immune = False

risk = age or chronic or immune

if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")
