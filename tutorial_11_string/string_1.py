# male -> ramesh, suresh, mukesh
# female -> sita, gita, rita

# student -> marks, name, start_date
# employee -> name, salary, joindate
# singer -> name, album

movie = "suPEr"

print(f"Type: {type(movie)}") # str calss is category

# print(f"Six Last char: {movie[-6]}")
print(f"Fifth Last char: {movie[-5]}")
print(f"Forth char: {movie[-4]}")
print(f"Third Last char: {movie[-3]}")
print(f"Second Last char: {movie[-2]}")
print(f"Last char: {movie[-1]}")
print(f"First char: {movie[0]}")
print(f"Second char: {movie[1]}")
print(f"Third char: {movie[2]}")
print(f"Fourth char: {movie[3]}")
print(f"Fifth char: {movie[4]}")
# print(f"Sixth char: {movie[5]}")

print(f"Total chars: {len(movie)}")
print(f"Last char: {movie[len(movie)-1]}")

# SUPER
print(f"First 3 chars: {movie[0:3]}") # SUP
print(f"First 3 chars: {movie[:3]}") # SUP

print(f"First 3 chars and ignore first: {movie[1:3]}") # UPE

print(f"---: {movie[1:]}") # UPER


print(f"Upper - {movie.upper()}")
print(f"Lower - {movie.lower()}")
print(f"Cap - {movie.capitalize()}")


# suPErmAN -> Superman
# write code to print capitalized string