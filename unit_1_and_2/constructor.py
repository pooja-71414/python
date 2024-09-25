class student:
    name='tybca'
    # default constructor.

    def __init__(self):
        print('default constructor..')

    # parameterized constructor.

    def __init__(self,name):
        self.name=name
        print('default constructor..')
        print(self.name)

# s=student()
s1=student('computer')
print(student.name)