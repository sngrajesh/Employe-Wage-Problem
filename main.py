import random

def check_attendance(name):
    # Generate a random attendance value between 0 and 1
    attendance = random.uniform(0, 1)
    if attendance:
        print(f'Employee {name} is present')
    else:
        print(f'Employee {name} is absent')

name = input('Enter your name: ')
if len(name) > 3 and name.isalpha():
    check_attendance(name)
else:
    print('Enter a valid name')

