import os
from datetime import datetime

# print(dir(os))

print(os.getcwd())

# os.chdir(r'C:\Users\MD. Nobin\PycharmProjects')
# print(os.getcwd())

# os.makedirs('newd3/newtest2')
# os.removedirs('newd3/newtest2')
# os.rmdir('newd2/get2')
# os.removedirs('newd2/get2')
# os.rename('newd', 'empty') 
# print(os.listdir())
# print(os.stat('empty'))
# print(os.stat('empty').st_size)

# mod_time = os.stat('empty').st_mtime
# print(datetime.fromtimestamp(mod_time))




# os.chdir(r'C:\Users\MD. Nobin\PycharmProjects\Corey Schafer')
# print(os.getcwd())
# os.makedirs('New')

print(os.environ.get('USERPROFILE'))
print(os.path.exists('/temp/test.txt'))
print(os.path.isfile('/temp/test.txt'))
print(os.path.isdir('/temp/test.txt'))
print(os.path.splitext('/temp/test.txt'))
print(dir(os.path))
'''

for dirpath, dirnames, filenames in os.walk(r'C:/Users/MD. Nobin/ PycharmProjects'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)

'''