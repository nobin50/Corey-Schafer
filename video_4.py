courses = ['History', 'Math', 'Physics', 'Chemistry']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])
courses.append('Art')
print(courses)
courses.insert(0, 'CompSci')
print(courses)

courses2 = ['Art', 'Education']
courses.insert(0, courses2)
print(courses)
print(courses[0])

courses = ['History', 'Math', 'Physics', 'Chemistry']
courses.extend(courses2)
print(courses)
courses.append(courses2)
print(courses)

courses.remove('Art')
print(courses)

courses.pop()
print(courses.pop())
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

num = [1,4,6,8,3,5]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

courses = ['Biology', 'Science', 'Aeroplane', 'Ticket']
sorted_courses = sorted(courses)
print(sorted_courses)
print(courses)


num = [1, 4, 6, 8, 3, 5]
print(min(num))
print(max(num))
print(sum(num))


courses = ['Biology', 'Science', 'Aeroplane', 'Ticket']
print(courses.index('Ticket'))
print('Aeroplane' in courses)

for item in courses:
    print(item)

for index, courses in enumerate(courses):
    print(index, courses)

courses = ['Biology', 'Science', 'Aeroplane', 'Ticket']
for index, courses in enumerate(courses, start=1):
    print(index, courses)


courses = ['Biology', 'Science', 'Aeroplane', 'Ticket']
courses_str = ', '.join(courses)
print(courses_str)


courses = ['Biology', 'Science', 'Aeroplane', 'Ticket']
courses_str = ' - '.join(courses)
print(courses_str)
new_str = courses_str.split(' - ')
print(new_str)


list_1 = ['Biology', 'Science', 'Aeroplane', 'Ticket']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Math'
print(list_1)
print(list_2)


tuple_1 = ('Biology', 'Science', 'Aeroplane', 'Ticket')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

"""
tuple_1[0] = 'Math'
print(tuple_1)
print(tuple_2)
"""


sets_1 = {'Biology', 'Science', 'Aeroplane', 'Ticket', 'Billiard'}
print(sets_1)

sets_2 = {'Biology', 'Radio', 'Science', 'Aeroplane', 'Ticket', 'Science'}
print(sets_2)
print('Radio' in sets_2)



sets_1 = {'Biology', 'Science', 'Aeroplane', 'Ticket', 'Billiard'}

sets_2 = {'Biology', 'Radio', 'Science', 'Aeroplane', 'Ticket', 'Science'}

print(sets_1.intersection(sets_2))
print(sets_1.difference(sets_2))
print(sets_1.union(sets_2))



empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # This is not working coz its empty dictionary
empty_set = set()
