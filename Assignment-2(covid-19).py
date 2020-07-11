class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


while True:

    while True:
        age = input("Are you a " + color.BOLD + "cigarette " + color.END +
                    "addict older than " + color.BOLD + "75 " + color.END + "years old? Yes or No: ").title().strip()
        if age == "Yes":
            age = True
            break
        elif age == "No":
            age = False
            break
        else:
            print("Try again and be carreful !!!")

    while True:
        chronic = input("Do you have a " + color.BOLD +
                        "severe " + color.END + "chronic disease? Yes or No: ").title().strip()
        if chronic == "Yes":
            chronic = True
            break
        elif chronic == "No":
            chronic = False
            break
        else:
            print("Try again and be carreful !!!")

    while True:
        immune = input("Is your " + color.BOLD + "immune " + color.END +
                       "system " + color.BOLD + "too weak" + color.END + "? Yes or No: ").title().strip()
        if immune == "Yes":
            immune = True
            break
        elif immune == "No":
            immune = False
            break
        else:
            print("Try again and be carreful !!!")

    risk = age or chronic or immune

    if risk == True:
        print("You are in risky group")
    else:
        print("You are not in risky group")
    break
