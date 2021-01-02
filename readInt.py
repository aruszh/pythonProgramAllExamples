def readInt(prompt, min, max):
    l=True
    while (l):
        try:
            prompt=int(input("Enter The Input In Integer"))
            if prompt>max or prompt<min:
                print("Enter no in range",min,max,sep=" ")
                continue
            l=False
            return prompt
        except ValueError:
            print("Enter Only Number")

    



v = readInt("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)