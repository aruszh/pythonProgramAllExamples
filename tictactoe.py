import time
board=[[i for i in range(0,3)]for j in range(0,3)]
k=1
mainList=[5]
compList=[5]
userList=[]
print("No. Selected By Computer --> 5")
for i in range(0,3):
    for j in range(0,3):
        if i==1 and j==1:
            board[i][j]='x'
            k+=1
            continue
        board[i][j]=k
        k+=1

def displayBoard():
    for i in range(0,3):
        print(board[i])
def userInput():
    boxNo=True
    
    while(boxNo):
        user=int(input("Please Enter Your Box No."))
        if user<=0 or user>9:
            print("Please Enter No Between 1-9")
        elif user in mainList:
            print("Already Occupied, Please Enter Free Space Box No")

            print("occupied space Box No",mainList,sep="\n")
        else:
            comp=user-1
            i=comp//3
            j=comp%3
            board[i][j]='O'
            userList.append(user)
            mainList.append(user)
            print("No selected by you --> ",user)
            print("All occupied space Box No's",mainList,sep="\n")  
              
            boxNo=False
    return user


def compInput():
    boxNo=True
    n=-1
    done=1
    while(boxNo):
        comp=userList[n]
        comp=comp*1504
        comp=comp%10
        comp=comp*21
        comp=comp%10
        print("done", done, "time with value --> ",comp)
        if comp<=0 or comp>9:
            n=n-1
            done=done+1
            continue
        elif comp in mainList:
            print("Already Occupied, Please Enter Free Space Box No")

            print("occupied space Box No",mainList,sep="\n")
            done=done+1
            n=n-1
            continue
        else:
            comp=comp-1
            i=comp//3
            j=comp%3
            board[i][j]='X'
            comp=comp+1
            compList.append(comp)
            mainList.append(comp)
            print("No selected by you --> ",comp)
            print("All occupied space Box No's",mainList,sep="\n")  
              
            boxNo=False
    return comp
    





gameOn=True
displayBoard()
while(gameOn):
    user=userInput()
    displayBoard()
    print("Comp Playing Its Turn")
    time.sleep(1)
    comp=compInput()
    time.sleep(1)
    displayBoard()
    if len(userList)==9:
        gameOn=False






