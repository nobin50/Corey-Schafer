class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.increment)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return 'Hurray! It\'s holiday'

        else:
            return 'Go to work.'


import datetime
my_date = datetime.date(2018, 7, 16)
print(Employee.is_workday(my_date))


"""
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Kenedy-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
"""


'''
emp_1 = Employee('Nihan', 'Walid', 50000)
emp_2 = Employee('Sadik', 'Sulaiman', 60000)




print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


emp_1.raise_amt = 1.05

print('After changing instance of emp_1')
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

'''