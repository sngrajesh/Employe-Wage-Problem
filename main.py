import random

class EmployeeAttendance:
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    PART_TIME_HOUR = 4
    
    @staticmethod
    def check_attendance():
        """
        Description : Generate Random number and check Employee is present or not 
        Input : None
        Output : {attendance} of 1 day
        """
        attendance = random.randint(0, 2)
        return attendance
    
    @classmethod
    def calculate_daily_wage(cls, attendance):
        """
        Description : Calculate daily wage of employee based on their attendance
        Input : {attendance} of one day
        Output : {wage, hour} object calculated 
        """
        match attendance:
            case 0:
                return {'wage': cls.WAGE_PER_HOUR * cls.FULL_DAY_HOUR, 'hour': 8}
            case 1:
                return {'wage': cls.WAGE_PER_HOUR * cls.PART_TIME_HOUR, 'hour': 4}
            case _:
                return {'wage': 0, 'hour': 0}
    
    @classmethod
    def monthly_wage_of_employee(cls):
        """
        Description : Calculate monthly wage of employee based on their attendance and limit of working hour
        Input : None 
        Output : {monthly_wage} of month
        """
        monthly_wage = 0
        total_hour = 0
        
        for i in range(0, 20):
            data = cls.calculate_daily_wage(cls.check_attendance())
            monthly_wage += data['wage']
            total_hour += data['hour']
            if total_hour >= 100:
                break
        
        return {'monthly_wage': monthly_wage, 'total_hour': total_hour}



if __name__ == "__main__":
    employee = EmployeeAttendance()
    data = employee.monthly_wage_of_employee()
    print(f"Wage is {data['monthly_wage']} for {data['total_hour']}")