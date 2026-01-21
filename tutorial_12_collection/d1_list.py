import time 
# stds = []
stds = ["Ramesh", "Suresh"]

print(type(stds))
# CRUD

# create / add
stds.append("Himesh")
stds.append("Mukesh")
stds.append("Ganesh")

# read 
print("First val:",stds[0])
print("Last val:",stds[-1])

print(stds)

# read all stdeunt 
for i in range(len(stds)):
    print(f"{i} -> {stds[i]}")
    # time.sleep(2)


# Update
stds[3] = "Mahesh"

print(stds)

stds.remove("Mahesh")

print(stds)
