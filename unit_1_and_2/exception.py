try:
    print('for exception')
    
except NameError:
    print('not defined variable')
except ZeroDivisionError:
    print('devide by zero is not defined')
except:
    print('exception occured')

else:
    print('in program does not occure exception..')
