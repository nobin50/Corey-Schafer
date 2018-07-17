
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)


with open('test.txt', 'r') as f1:
    line = f1.readline()
    print(line)

with open('test.txt', 'r') as f2:
    lines = f2.readlines()
    print(lines)

with open('test.txt', 'r') as f3:
    line = f3.readline()
    print(line, end='')

    line = f3.readline()
    print(line, end='')


with open('test.txt', 'r') as fl:
    for line in fl:
        print(line, end='')

with open('test.txt', 'r') as f:
    content = f.read(50)
    print(content)

with open('test.txt', 'r') as f:
    size = 59
    content = f.read(size)
    print(content)
    print(f.tell())


with open('test2.txt', 'w') as f:
    f.write('I am new file')
    f.seek(0)
    f.write('I am overwritten')


with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


with open('tst.jpg', 'rb') as rf:
    with open('tst_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
