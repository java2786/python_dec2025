# movie = "  super "
movie = "     superman is comming from Crypton     "

print(f"Length: {len(movie)}")
print(f"Length: {len(movie.strip())}")
movie = movie.strip()
print(f"-{movie.title()}-")

print(movie.__len__())