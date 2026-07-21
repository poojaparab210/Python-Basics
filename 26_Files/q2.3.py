with open("task.txt","r")as f:
    for line in f:
        print(line)
    f.close()

    #  or
    for line in f.readlines():
        print(line)