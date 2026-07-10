marks = [5,2,21,5,7]
extra_marks = [53,23,32]
print(marks)
marks.append(63)    #  Adds an element at the end of the list.
print(marks)

marks.pop()     # Removes the element at a specific index or the last element if no index is specified
print(marks)

marks.extend(extra_marks)       # Adds multiple elements to the end of the list.
print(marks)

marks.insert(1,6)  # Adds an element at a specific position.
print(marks) 

marks.reverse() # it will reverse the list
print(marks)

marks.sort() # it will give in asecending order
print(marks)

