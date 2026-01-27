# filename = "movies.txt"
filename = "/Volumes/My Shared Files/shared/thispc_host/python_dec2025/tutorial_13/movies.txt"

with open(filename, "a") as file_obj:
    print("File opening is done")
    # file is not empty for append
    file_obj.write("\nRRR")
    
print("Bye Bye")