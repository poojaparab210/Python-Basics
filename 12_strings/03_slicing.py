# You can extract parts of a string using slicing:

name = "Pooja0123456789"

print(name[0:2]) # goes from 0 to 2-1 (ie., 0 to 1)
print(name[2:-1]) # Same as name [2:4]

# print(name[0:10:n]) # Skip n-1 characters
print(name[0:10:1]) # Skip 0 characters
print(name[0:10:2]) # Skip 1 (2-1)characters
print(name[0:10:3]) # Skip 2 (3-1)characters

print(name[:4]) # Replace the 1st empty no. with 0 (name[0:4])
print(name[1:]) # replace the 2nd empty no. with lenght (name[1:15])