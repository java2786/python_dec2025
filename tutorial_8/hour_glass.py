def generateHourGlass(rows):
    # rows = 16
    cols = rows

    for row in range(1,rows+1):
        for col in range(1,cols+1):
            if(row==1 or row==rows):
                print("* ",end="",sep="")
            elif(row==col):
                print("* ",end="",sep="")
            elif(row+col==rows+1):
                print("* ",end="",sep="")
            else:
                print("  ",end="",sep="")
        print()
        
        
        
generateHourGlass(3)
print("\n\n")
generateHourGlass(8)
print("\n\n")
generateHourGlass(15)
print("\n\n")
generateHourGlass(5)