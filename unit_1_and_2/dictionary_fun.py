dic1={
    1:'one',
    2:'two'
}
dic2={
    2:'two',
    3:'three'
}
print('type(dic1) = ',type(dic1))
print('dic1.keys(),dic2.keys() = ',dic1.keys(),dic2.keys())
print('dic1.values(),dic2.values() = ',dic1.values(),dic2.values())
print('dic1.items(),dic2.items() = ',dic1.items(),dic2.items())
print('len(dic1) = ',len(dic1))
# print('len(dic2) = ',len(dic2))
print('str(dic1) = ',str(dic1))
# print('str(dic2) = ',str(dic2))
print('fromkeys(dic2) = ',dic2.fromkeys('2'))