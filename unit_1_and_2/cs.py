'''
# if statement
a=int(input("enter a = "))
print(a)
if a>0:
    print("value of a is positive")
# if...else statement
a=int(input("enter a = "))
print(a)
if a>0:
    print("value of a is positive")
else :
    print("value of a is negative")
# if...elif.. else statement
a=int(input("enter a = "))
print(a)
if a>0:
    print("value of a is positive")
elif a==0 :
    print("value of a is zero")
else :
    print("value of a is negative")
'''
# nested if statement
no=int(input('enter a no = '))
if no>0:
    if no>9999:
        print('five digit number')
    elif no>999:
        print('four digit number')
    elif no>99:
        print('three digit number')
    elif no>9:
        print('two digit number')
    elif no>0:
        print('one digit number')
elif no==0:
    print('number is zero')
else:
    print('negative number')    
