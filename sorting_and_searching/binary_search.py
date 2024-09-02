pos=0
def binarysearch(list,n):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if list[mid]==n:
            pos=mid
            globals()['pos']=mid
            return True
        elif list[mid]>n:
            high=mid-1
        elif list[mid]<n:
            low=mid+1
    
list=[0,1,2,3,4,5,6,7,8,9,10]
n=int(input('enter search item = '))
if binarysearch(list,n):
    print('item founded in ',pos,' position')
else:
    print('item not founded in this list')