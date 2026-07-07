# Recursion in Python
# A function calling itself to solve a problem.

# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1
# The series begins: \(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,.....
# ex:
# 0 1 1 2 3 5 8 13

'''fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1)
'''
# Important Notes:
# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals.

def fib(n):
    # base case of recursion:
    if(n == 0 or n == 1):
        return n
    #      fib(4)   +   fib(5)
    return fib(n-2) + fib(n-1)
print(fib(6))

# This is how calculate the fibonacci series:
'''
fib(4)  + fib(5)
fib(2)  + fib(3)  + fib(5)
fib(0)  + fib(1)  + fib(3) + fib(5)
0 + 1   + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0)  + fib(1) + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1
'''

