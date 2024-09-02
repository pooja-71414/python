'''
def linearsearch(list,n):
    for i in range(0,len(list)):
        if list[i]==n:
            print('item founded in = ',i)
            break
        elif i==len(list)-1:
            print('item not founded')

list=[0,1,2,3,4,5,6,7,8,9,10]
n=int(input('enter search item = '))
linearsearch(list,n)
'''


pos=0
def linearsearch(list,n):
    for i in range(0,len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True

list=[0,1,2,3,4,5,6,7,8,9,10]
n=int(input('enter search item = '))
if linearsearch(list,n):
    print('item founded in ',pos,' position')
else:
    print('item not founded')