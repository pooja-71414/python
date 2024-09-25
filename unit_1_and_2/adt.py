class stack:
    def __init__(self) -> None:
        self.item=[]

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if self.item is not None:
            return self.item.pop()
s=stack()
print(s.item)
s.push('one')
s.push('two')
s.push('three')
s.push('four')
s.push('five')
print(s.item)
s.pop()
print(s.item)