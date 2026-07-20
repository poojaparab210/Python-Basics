def marks(**kwargs):
    # kwargs is dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} are {kwargs[item]}")

marks(payal = 50,vidhika = 54, marie = 90 )