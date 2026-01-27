filename = "movies.txt"

with open(filename, "r") as file_obj:
    print("File opening is done")
    # file is not empty for append
    lines = file_obj.readlines()
    for line in lines:
        print(line, end="")
    
print("\n\nBye Bye")