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
    Output : {wage, hour} object calculated 
    """
    match attendance:
        case 0:
            return {'wage' : WAGE_PER_HOUR*FULL_DAY_HOUR, 'hour' : 8}
        case 1:
            return {'wage' : WAGE_PER_HOUR*PART_TIME_HOUR, 'hour' : 4}
        case _:
            return {'wage' : 0, 'hour' : 0}



def monthly_wage_of_employee ():
    """
    Description : Calcualate monthly wage of employee based on their atendance on attendance and limit of working hour
    Input : None 
    Output : {monthly_wage} of month
    """

    monthly_wage = 0
    total_hour = 0
    
    for i in range(0,20):
        data = calculate_daily_wage(check_attendance())
        monthly_wage += data['wage']
        total_hour += data['hour']
        if(total_hour >= 100):
            break

    return {'monthly_wage' : monthly_wage,'total_hour':total_hour}
    


name = input('Enter your name: ')
if len(name) > 3 and name.isalpha():
    data = monthly_wage_of_employee()
    print(f"{name} wage is {data['monthly_wage']} for {data['total_hour']}")
else:
    print('Enter a valid name')
