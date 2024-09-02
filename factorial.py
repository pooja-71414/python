no= int(input('entr no = '))
fact=1
if no<0:
    print('does not exist...')

elif no==0:
    print('0 factorial is 1')

else:
    for i in range(1,no+1):
        fact=fact*i
    print('ans = ',fact)