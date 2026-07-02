age = int(input("Enter your age:"))

if(age>18):
    print("You can Drive")
elif(age==18):
    print("Lets schedule your interview")
elif(age == 0):
    print("Hey you are just born")
else:
    print("Sorry you cannot drive")
