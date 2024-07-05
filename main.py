import random

class EmployeeAttendance:
    @staticmethod
    def check_attendance():
        """
        Description : Generate Random number and check employee is present or not
        Input : Node
        Output: {attendance} of 1 day (0: Full day, 1: Part time, 2: Absent)
        """
        return random.randint(0, 2)

    @staticmethod
    def calculate_daily_wage(attendance, wage_per_hour, full_day_hours, part_time_hours):
        """
        Description : Calculate daily wage of employee based on their attendance
        Input: attendance of one day, wage per hour, full day hours, part time hours
        Output: {wage, hours} object
        """

        match attendance:
            case 0:
                return {'wage': wage_per_hour * full_day_hours, 'hours': full_day_hours}
            case 1:
                return {'wage': wage_per_hour * part_time_hours, 'hours': part_time_hours}
            case _:
                return {'wage': 0, 'hours': 0}

    @classmethod
    def monthly_wage_of_employee(cls, company_name, wage_per_hour, working_days_per_month, max_hours_per_month, full_day_hours, part_time_hours):
        """
        Calculate monthly wage of employee based on their attendance and company-specific parameters
        Input: company name, wage per hour, working days per month, max hours per month, full day hours, part time hours
        Output: {monthly_wage, total_hours, company} of month
        """

        monthly_wage = 0
        total_hours = 0

        for _ in range(working_days_per_month):
            if total_hours >= max_hours_per_month:
                break
            
            daily_data = cls.calculate_daily_wage(
                cls.check_attendance(),
                wage_per_hour,
                full_day_hours,
                part_time_hours
            )
            
            monthly_wage += daily_data['wage']
            total_hours += daily_data['hours']

            if total_hours > max_hours_per_month:
                total_hours = max_hours_per_month
                monthly_wage = total_hours * wage_per_hour
                break

        return {
            'monthly_wage': monthly_wage,
            'total_hours': total_hours,
            'company': company_name
        }

def main():
    employee = EmployeeAttendance()
    
    companies = [
        {
            'name': 'BridgeLabz',
            'wage_per_hour': 20,
            'working_days_per_month': 22,
            'max_hours_per_month': 100,
            'full_day_hours': 8,
            'part_time_hours': 4
        }
    ]
    
    for company in companies:
        data = employee.monthly_wage_of_employee(
            company['name'],
            company['wage_per_hour'],
            company['working_days_per_month'],
            company['max_hours_per_month'],
            company['full_day_hours'],
            company['part_time_hours']
        )
        print(f"For {data['company']}: Wage is ${data['monthly_wage']} for {data['total_hours']} hours")

if __name__ == "__main__":
    main()
