import os

os.chdir(r'C:\Users\MD. Nobin\PycharmProjects\Corey Schafer\New')
print(os.getcwd())

listoffiles =[
    'Earth - Our Solar System - #4.mp4',
    'Jupiter - Our Solar System - #6.mp4',
    'Mars - Our Solar System - #5.mp4',
    'Mercury - Our Solar System - #2.mp4',
    'Neptune - Our Solar System - #8.mp4',
    'Pluto - Our Solar System - #10.mp4',
    'Saturn - Our Solar System - #7.mp4',
    'The Sun - Our Solar System - #1.mp4',
    'Uranus - Our Solar System - #9.mp4',
    'Venus - Our Solar System - #3.mp4']

for fname in listoffiles:
    with open(fname, 'a'):
        pass

print('Complete')


for f in os.listdir():
    print(f)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)

    os.rename(f, new_name)




