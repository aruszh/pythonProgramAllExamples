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
        list2=self.__stackList
        print(list2)


    

stackObject = stack()

stackObject.display()
stackObject.push(2)
stackObject.display()
stackObject.pop()
stackObject.display()

class addInStack(stack):
    def __init__(self):
        stack.__init__(self)
        self.__sum=0
    def push(self,value):
        self.__sum+=value
        stack.push(self,value)

    def pop(self):
        val1=stack.pop
        self.__sum-=val1

    def getSum(self):
        return self.__sum
    

stackObject2=addInStack()
stackObject2.push(3)
stackObject2.display()

print(stackObject2.getSum())
