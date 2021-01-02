blocks = int(input("Enter the number of blocks: "))
s=0
c=0
for i in range(blocks):
    if blocks<s:
        break
    s+=1
    c+=1
    blocks-=s
    

print("The height of the pyramid:",c)