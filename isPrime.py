def isPrime(num):

    c=0
    for i in range(1,num):
        if num%i==0:
            c=c+1

    if (c==1):
        return True
    if (c!=1):
        return False
    
for i in range(1, 20):
	if isPrime(i + 1):
		print(i + 1, end=" ")
print()