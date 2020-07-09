age = input("Are you a cigarette addict older than 75 years old? \nEnter Yes or No?").title().strip()

if age == "Yes":
    age = True

else: age = False

chronic = input("Do you have a severe chronic disease? \nEnter Yes or No?").title().strip()

if chronic == "Yes":
    chronic = True
else: chronic = False

immune = input("Is your immune system too weak? \nEnter Yes or No?").title().strip()

if immune == "Yes":
    immune = True
else: immune = False

if (age or chronic or immune):
    print("You are in risky group")

else : print("You are not in risky group")