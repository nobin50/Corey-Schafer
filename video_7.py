nums = [1, 2, 3, 4]
for num in nums:
    print(num)

print('Using break')
nums = [1, 2, 3, 4]
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)


print('Using Continue')
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)



nums = [1, 2, 3, 4]
for num in nums:
    for letter in 'abcd':
        print(num, letter)


print('Range')
for i in range(10):
    print(i)

print('1 to 10')
for i in range(1,11):
    print(i)


print('While Loop')
x = 8

while x < 10:
    print(x)
    x += 1


print('While Loop')
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


print('While Loop')
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1


print('Keyboard interrupt is Ctrl + C')