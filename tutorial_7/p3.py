"""
r c->
|    1 2 3 4 5
1 -> * * * * *
2 -> *       *
3 -> *       *
4 -> *       *
5 -> *       *
6 -> *       *
7 -> * * * * *


"""

rows = 8
cols = 5

for row in range(1, rows+1):
    for col in range(1, cols+1):
        if(row==1 or row==rows or col==1 or col==cols):
            # print(row,col," ", sep="",end="")
            # print(row,col, sep="",end="")
            
            print("* ", sep="",end="")
        else:
            # print("#  ",end="")
            # print("# ",end="")
            print("  ",end="")
        # print("* ", end="")
    print()    
