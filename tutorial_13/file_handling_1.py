filename = "movies.txt"

with open(filename, "w") as file_obj:
    print("File opening is done")
    # file is empty
    file_obj.write("Bahubali")
    file_obj.write("\n")
    file_obj.write("Pushpa")
    
print("Bye Bye")