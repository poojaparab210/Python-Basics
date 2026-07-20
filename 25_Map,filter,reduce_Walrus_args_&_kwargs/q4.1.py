# Create a class Book with attributes title and author .
# 1. IMplement __str__() so that printing the object displays "Title by author"
# 2. IMplement __len__() so that len(Book) return the length of the title

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)
    
p1 = Book("Power of python","Marie")
print(len(p1))
print(p1)

p2 = Book("Java","Jack")
print(len(p2))
print(p2)
