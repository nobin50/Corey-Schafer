person = {'name': 'John', 'age': 26}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

sentence1 = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence1)

sentence1 = 'My name is {1} and I am {0} years old'.format(person['name'], person['age'])
print(sentence1)


sentence1 = 'My name is {0[name]} and I am {1[age]} years old'.format(person, person)
print(sentence1)


sentence1 = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence1)


l = ['Jenny', 24]
sentence = 'Hi!, I am {} and I am {} years old.'.format('Jenny', 24)
print(sentence)


l = ['Jenny', 24]
sentence = 'Hi!, I am {0[0]} and I am {0[1]} years old.'.format(l)
print(sentence)


tag = 'hi'
text = 'This is a headline'
sentence = '<{0}>{1}<{0}>'.format(tag, text)
print(sentence)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Dany', 37)

sentence = 'Hi!, I am {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


sentence = 'Hi!, I am {name} and I am {age} years old.'.format(name='Luke', age=34)
print(sentence)


person = {'name': 'John', 'age': 26}
sentence = 'Hi!, I am {name} and I am {age} years old.'.format(**person)
print(sentence)


for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)


for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)


pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)


sentence = '1 Mb is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)


import datetime

my_date = datetime.datetime(2018, 7, 18, 12, 43, 45)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
