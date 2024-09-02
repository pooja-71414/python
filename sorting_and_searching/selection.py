def selection(num):
    for i in range(len(num)-1):
        minpos=i
        for j in range(i,len(num)):
            if num[j]<num[minpos]:
                minpos=j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp

num=[87,98,4,79,30,29,80]
print(num)
selection(num)
print(num)