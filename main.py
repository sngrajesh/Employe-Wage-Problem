import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

def check_attendance(name):
    # Generate a random attendance value between 0 and 1
    attendance = random.randint(0, 2)
    if attendance == 0:
        print(f'Employee {name} is present')
    elif attendance == 1:
        print(f'Employee {name} is on Part-time')
    else:
        print(f'Employee {name} is absent')
    
    return attendance

def calculate_daily_wage(attendance):
    if attendance == 0:
        return WAGE_PER_HOUR*FULL_DAY_HOUR
    elif attendance == 1:
        return WAGE_PER_HOUR*PART_TIME_HOUR
    else:
        return 0


name = input('Enter your name: ')
if len(name) > 3 and name.isalpha():
    attendance = check_attendance(name)
    print(f'{name} wage is {calculate_daily_wage(attendance)}')
else:
    print('Enter a valid name')
