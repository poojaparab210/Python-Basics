# Create a class MathUtils with:
# 1. A @staticmethod called add(a,b) that return a+b
# 2. A@classmethod called description(cls) that prints "This is a utility class for math operations"

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operation")
        
    
a = MathUtils
print(a.add(3,5))
a.description()

# Or
MathUtils.description()
print(MathUtils.add(3,6))