import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

def check_attendance(name):
    # Generate a random attendance value between 0 and 1
    attendance = random.uniform(0, 1) > 0.5
    if attendance:
        print(f'Employee {name} is present')
    else:
        print(f'Employee {name} is absent')
    return attendance

def calculate_daily_wage(attendance):
    if attendance:
        return WAGE_PER_HOUR*FULL_DAY_HOUR
    else:
        return 0


name = input('Enter your name: ')
if len(name) > 3 and name.isalpha():
    attendance = check_attendance(name)
    print(f'{name} wage is {calculate_daily_wage(attendance)}')
else:
    print('Enter a valid name')
