import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

def check_attendance(name):
    """
    Descrption : Generate Random number and check Employee is present or not 
    Input : {name} of the employee
    Output : {attendance} of 1 day
    """

    # Generate a random attendance value between 0 and 1
    attendance = random.randint(0, 2)
    match attendance:
        case 0:
            print(f'Employee {name} is present')
        case 1:
            print(f'Employee {name} is on Part-time')
        case _:
            print(f'Employee {name} is absent')
    return attendance

def calculate_daily_wage(attendance):
    """
    Descrption : Calcualate daily wage of employee based on their atendance on attendance
    Input : {attendance} of one day
    Output : {wag} calculated 
    """
    match attendance:
        case 0:
            return WAGE_PER_HOUR*FULL_DAY_HOUR
        case 1:
            return WAGE_PER_HOUR*PART_TIME_HOUR
        case _:
            return 0


name = input('Enter your name: ')
if len(name) > 3 and name.isalpha():
    attendance = check_attendance(name)
    print(f'{name} wage is {calculate_daily_wage(attendance)}')
else:
    print('Enter a valid name')
