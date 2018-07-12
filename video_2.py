print('Hello World')
message = 'Hello World'
print(message)
print("Bobby's World")
print('Bobby\'s World')
my_message = """Bobby's World was a good
cartoon in the 1990s"""
print(my_message)
print(len(message))
print(message[0])
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))

message = 'Hello World'
new_message = message.replace('World', 'Universe')
print(new_message)
message = message.replace('World', 'Bangladesh')
print(message)

greeting = 'Hello'
name = 'Micheal'

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))
print(help(str))
print(help(str.lower))
