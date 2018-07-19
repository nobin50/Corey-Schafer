import datetime
import pytz

a = [1, 2, 3, 4]
b = 'sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

# The goal of __repr__ is to be unambiguous

# The goal of __str__ is to be readable


a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

print()
print("str(a): {}".format(str(a)))
print("str(b): {}".format(str(b)))
print()

print("repr(a): {}".format(repr(a)))
print("repr(b): {}".format(repr(b)))
