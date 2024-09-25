# function arguments
# 1.require argument

'''def udf(a):
    print(a)

print('UDF using a require argument')
a=input('enter int value = ')
udf(a)'''

# 2.keyword argument

'''def udf(name):
    print(name)

print('UDF using a keyword argument')
value=input('enter a value = ')
udf(name=value)'''

# 3.default argument

'''def udf(a,name='default'):
    print(a,name)

print('UDF using a default argument')
# a=input('enter int value = ')
# name=input('enter a name = ')
udf(12,'given')
udf(67)'''

# 4.variable length argument

'''def udf(arg1,*t):
    print(arg1)
    for i in t:
        print(i)

udf(1,2,3,4,5,6,7)
udf(10,20,40)
udf(50)
udf(40)'''