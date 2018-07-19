li = [9, 1, 8, 7, 3, 6, 4, 2, 5]
s_li = sorted(li)
print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)
li.sort()
print('Sort Variable:\t', li)


li = [9, 1, 8, 7, 3, 6, 4, 2, 5]
s_li = sorted(li, reverse=True)
print('Reverse Sorted Variable:\t', s_li)
print('Original Variable:\t', li)
li.sort(reverse=True)
print('Reverse Sort Variable:\t', li)


tup = (9, 1, 8, 7, 3, 6, 4, 2, 5)
s_tup = sorted(tup)
print('Tuple Sorted Variable:\t', s_tup)
print('Original Variable:\t', tup)
s_tup = sorted(li, reverse=True)
print('Reverse Tuple Variable:\t', s_tup)
print('Original Variable:\t', tup)


di = {'name': 'Corey', 'job': 'programming', 'age': 47, 'os':'Mac'}
s_di = sorted(di)
print('Dict:\t', s_di)


li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(s_li)


li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_emp = sorted(employees, key=e_sort)
print(s_emp)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_emp = sorted(employees, key=e_sort, reverse=True)
print(s_emp)


from operator import attrgetter


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


s_emp = sorted(employees, key=attrgetter('age'))
print(s_emp)