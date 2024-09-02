def bubble(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
num=[89,57,435,97,4,87,90]
print(num)
bubble(num)
print(num)