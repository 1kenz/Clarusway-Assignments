while True:
    num = input("Enter a integer number: ")
    if not num.isdigit():
        print("Please enter an positive integer number !!!")
    else:
        break

num_int = int(num)
digit = str(num)
sum = 0

for i in digit:
    power = int(i)**len(digit)
    sum += power
if (num_int == sum):
    print(f"{num_int} is a Armstrong number.")
else:
    print(f"{num_int} is NOT a Armstrong number.")
