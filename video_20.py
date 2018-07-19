nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n for n in nums]
print(my_list)


my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list = [n*n for n in nums]
print(my_list)

my_list = map(lambda n: n*n, nums)
print(my_list)

my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)


my_list = {n for n in nums if n%2 ==0}
print(my_list)

my_list = filter(lambda n: n%2 == 0, nums)
print(my_list)


my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)


my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)


names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolvarine', 'Deadpool']
print(zip(names, heroes))


nums = [1, 1, 2, 4, 4, 5, 5, 5, 9, 7, 8, 8]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

numb = [1, 3, 4, 5, 6, 7, 8, 9, 2]
def gen_func(numb):
    for n in numb:
        yield (n*n)


my_gen = gen_func(numb)

for i in my_gen:
    print(i)


print()
print('Short & easy')
my_gen = (n*n for n in numb)
for n in my_gen:
    print(n)