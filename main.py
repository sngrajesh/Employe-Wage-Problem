import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

def check_attendance():
    """
    Description : Generate Random number and check Employee is present or not 
    Input : None
    Output : {attendance} of 1 day
    """
    attendance = random.randint(0, 2)
    return attendance



def calculate_daily_wage(attendance):
    """
    Description : Calcualate daily wage of employee based on their atendance on attendance
    Input : {attendance} of one day
    Output : {waga} calculated 
    """
    match attendance:
        case 0:
            return WAGE_PER_HOUR*FULL_DAY_HOUR
        case 1:
            return WAGE_PER_HOUR*PART_TIME_HOUR
        case _:
            return 0  



def monthly_wage_of_employee ():
    """
    Description : Calcualate monthly wage of employee based on their atendance on attendance
    Input : None 
    Output : {monthly_wage} of month
    """

    monthly_wage = 0
    for i in range(0,20):
        monthly_wage += calculate_daily_wage(check_attendance())
    
    return monthly_wage
    


name = input('Enter your name: ')
if len(name) > 3 and name.isalpha():
    monthly_wage = monthly_wage_of_employee()
    print(f'{name} wage is {monthly_wage}')
else:
    print('Enter a valid name')
