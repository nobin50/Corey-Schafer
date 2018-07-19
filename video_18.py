import builtins

x = 'global x'


def test():
    global x
    x = 'local x'
    print(x)


test()
print(x)
print(dir(builtins))


def outer():
    x = 'Outer x'

    def inner():
        x = 'Inner x'
        print(x)

    inner()
    print(x)


outer()


print('3 format.....')
x = 'global x'

def outer():
    x = 'Outer x'

    def inner():
        x = 'Inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)


print('For nonlocal.....')
x = 'global x'


def outer():
    x = 'Outer x'

    def inner():
        nonlocal x
        x = 'Inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)
