from datetime import datetime

now = datetime.now()
current_year = int(now.year)

age = int(input("What is your age?: "))
years_till_100 = 100 - age
year_will_be_100 = current_year + years_till_100

print(
    f'You will be 100 in {years_till_100} years.\nIt will be the year {year_will_be_100}.')
