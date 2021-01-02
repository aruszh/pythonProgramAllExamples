board=[["new" for i in range(8)]for j in range(8)]

pawn="Pawn"

board[1][1]=pawn

for i in board:
    print(i,end="\n")