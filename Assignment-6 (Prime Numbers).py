number = int(input("Enter the number: "))

prime_list = []

for i in range(2, number+1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        prime_list.append(i)
print("Prime list = ", prime_list)
