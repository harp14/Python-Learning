from datetime import datetime

now = datetime.now()
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []

for year in years_of_birth:
    ages.append(now.year - year)

print(ages)
