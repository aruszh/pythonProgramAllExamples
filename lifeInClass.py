class exampleClass:
    pass

class exampleClass2:
    pass

class exampleClass3(exampleClass):
    pass

exampleObject1=exampleClass
exampleObject1.hello="hiiii"

exampleObject2=exampleClass

print(exampleClass.__dict__)
print(exampleClass.__name__)
print(exampleClass.__bases__)
print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject2.hello)
print(exampleObject1.__dir__)
print(exampleObject1.__bases__)
print(exampleClass3.__bases__)

print(issubclass(exampleClass3,exampleClass2),end="\t")
print(issubclass(exampleClass3,exampleClass))
