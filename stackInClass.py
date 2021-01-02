class stack:
    def __init__(self):
        self.__stackList=[]

    def push(self,value):
        self.__stackList.append(value)

    def pop(self):
        val=self.__stackList[-1]
        del self.__stackList[-1]
        return val
    def display(self):
        return self.__stackList

    

stackObject = stack()

print(stackObject.display())
stackObject.push(2)
print(stackObject.display())
stackObject.pop()
print(stackObject.display())

