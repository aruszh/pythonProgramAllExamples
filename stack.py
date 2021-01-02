stack=[]
def push(number):
    stack.append(number)

def pop():
    val=stack[-1]
    del stack[-1]
    return val

push(1)
push(2)
push(3)
print(stack)
pop()
print(stack)
print(pop())
print(stack)
