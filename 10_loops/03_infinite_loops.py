# Be careful to avoid infinite loops by ensuring the condition eventually becomes False.
# Example of an infinite loop:

i = 1
while i<6:   #  This loops will run forever because the condition is always True & it will print only 1 forever.
    print(i)
    i + 1