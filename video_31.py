try:
    f = open('textdocument.txt')
except Exception:
    print('The file does not exist')


try:
    f = open('textdocument.txt')
except FileNotFoundError:
    print('The file you want to open does not exist.')


try:
    f = open('text_document.txt')
    var = bad_var
except FileNotFoundError:
    print('The file you want to open does not exist.')
except Exception:
    print('Sorry! something went wrong')


try:
    f = open('text_document.txt')
except FileNotFoundError:
    print('The file you want to open does not exist.')
except Exception:
    print('Sorry! something went wrong')
else:
    print(f.read())
    f.close()


try:
    f = open('text_document.txt')
except FileNotFoundError:
    print('The file you want to open does not exist.')
except Exception:
    print('Sorry! something went wrong')
else:
    print(f.read())
    f.close()
finally:
    print('I will be printed whatever error or not.')


try:
    f = open('text_document.txt')
    if f.name == 'text_document.txt':
        raise Exception
except FileNotFoundError:
    print('The file you want to open does not exist.')
except Exception:
    print('Sorry! something went wrong')
else:
    print(f.read())
    f.close()
finally:
    print('I will be printed whatever error or not.')


