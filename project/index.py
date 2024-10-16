# import conn
from conn import dbdemo
# db=dbdemo()


while True:
    print()
    print('press 1 for Insert')
    print('press 2 for Fetch')
    print('press 3 for Delete')
    print('press 4 for Update')
    print('press 5 for Exit')
    print()

    try:
        choice=int(input('enter choice = '))

        if choice==1:
            pass

        elif choice==2:
            pass

        elif choice==3:
            pass

        elif choice==4:
            pass

        elif choice==5:
            pass

        else:
            print('invalid input! .. please try again!')

    except Exception as e:
        print('exception is = ',e)