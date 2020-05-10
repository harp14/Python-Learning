a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

in_both = []

for a_number in a:
    if (a_number in b) and (a_number not in in_both):
        in_both.append(a_number)

print(in_both)
