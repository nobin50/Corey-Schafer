if True:
    print('Condition is true')

if False:
    print('Condition is False')

language = 'Python'

if language == 'Python':
    print('It is true')

language = 'Java'
if language == 'Python':
    print('It is true')
else:
    print('No Match')

language = 'Java'
if language == 'Python':
    print('It is Python')
elif language == 'Java':
    print('It is Java')
else:
    print('No Match')


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creeds')


user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creeds')


user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creeds')


user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)


a = [1, 2, 3]
b = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))


condition = False
if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')


condition = None
if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')


condition = 0
if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')


condition = ""
if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')


condition = {}
if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')

