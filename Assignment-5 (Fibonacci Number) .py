number = int(input("Enter a number: "))
fibonacci = []

a = 0
b = 1

while (a < number):
    c, b = b, a
    a = c + b
    fibonacci.append(a)
print(fibonacci)