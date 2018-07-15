class Employee:
    employee_no = 0
    increment = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.employee_no += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.increment)


print(Employee.employee_no)
emp_1 = Employee('Nihan', 'Walid', 50000)
emp_2 = Employee('Sadik', 'Sulaiman', 60000)
print(Employee.employee_no)



emp_1.increment = 1.05
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.increment)
print(emp_1.increment)
print(emp_2.increment)

print(emp_2.__dict__)
print(emp_1.__dict__)
