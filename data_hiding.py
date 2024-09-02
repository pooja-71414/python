class dh:
    __var=1 # hide variable

    def count(self):
        self.__var+=1
        print(self.__var)

d=dh()
d.count() # print=2
d.count() # print=3
d.count() # print=4
# print(d.__var)
print(d._dh__var) # print=4