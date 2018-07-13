student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 1: 'Villain'}
print(student)
print(student['name'])
print(student['courses'])
print(student[1])
print(student.get('age'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))
student['name'] = 'Jane'
student['phone'] = '555-5555'
print(student)
student.update({'name': 'Duke', 'age': 26})
print(student)
del student['courses']
print(student)
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 1: 'Villain'}
cousrses = student.pop('courses')
print(cousrses)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
    