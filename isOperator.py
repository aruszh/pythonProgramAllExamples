class exampleClass:
    def __init__(self):
        self.hiiii=3

exampleObject1=exampleClass()
exampleObject2=exampleClass()

exampleObject2.hello=3

#exampleObject1.hiiii=3
print(exampleObject1.__dict__,exampleObject2.__dict__,sep="\n\n")
print(exampleObject1 is exampleObject2)
exampleObject3=exampleObject2
print(exampleObject2 is exampleObject3)