number_list = []

for i in range(1, 101):
    if i % 15 == 0:
        number_list.append("FizzBuzz")
    elif i % 3 == 0:
        number_list.append("Fizz")
    elif i % 5 == 0:
        number_list.append("Buzz")
    else:
        number_list.append(i)
for i in number_list:
    print(i, sep="\n")
