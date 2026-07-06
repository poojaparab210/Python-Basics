#Using format() , create a sentence:"My name is John and I am 25 years old."by passing "John" and 25 as variables.

text = "My name is {} and I am {} years old."
a1 = "Pooja"
a2 = "21"
s = text.format(a1,a2)
print(s)

# or

a1 = "Pooja"
a2 = "21"
print("My name is {} and I am {} years old.".format(a1,a2))