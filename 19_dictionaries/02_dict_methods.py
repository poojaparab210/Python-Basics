marks = {"Pooja": 50 , "Payal": 45 , "Lily": 94}

print(marks.keys())
print(marks.values())
print(marks.items())

marks.pop("Lily")
print(marks)

marks.popitem()
print(marks)

marks.clear()
print(marks)