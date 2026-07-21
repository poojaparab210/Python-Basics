# f = open("pooja.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("pooja.txt", "r") as f:  # Context Manager
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with syntax
