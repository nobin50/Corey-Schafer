class Employee:


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.increment)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Nihan', 'Walid', 50000)
emp_2 = Employee('Sadik', 'Sulaiman', 60000)
emp_3 = Employee('Luka', 'Sober', 40000)

print(emp_1.__repr__())
print(str(emp_2))
print(int.__add__(1, 2))
print(int.__mul__(3, 4))
print(emp_1 + emp_2) 
print(len(emp_3))

