to_divide = int(input("Enter number: "))
divisors = []

for number in range(1, to_divide):
    if to_divide % number == 0:
        divisors.append(number)

print(divisors)
