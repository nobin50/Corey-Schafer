print('Basic Function')


def square_nums(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_nums([1, 2, 3, 4, 5])
print(my_nums)


print('Generator by yeild')


def square_nums(nums):
    for i in nums:
        yield (i*i)


my_nums = square_nums([1, 2, 3, 4, 5])
for i in my_nums:
    print(i)


print('List comprehension')
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)


print('Generator')
my_nums = (x*x for x in [1, 2, 3, 4, 5])
for i in my_nums:
    print(i)

