class exampleClass:
    __counter=3
    hi=1504
    def __init__(self,val=1):
        self.__first=val
        self.__counter+=3


exampleObject1=exampleClass()
exampleObject2=exampleClass(4)
exampleObject2.__hello="hello"

print(exampleObject1.__dict__,exampleObject2.__dict__,sep="\n")
print(exampleObject2.__hello)
print(exampleObject2._exampleClass__counter)

