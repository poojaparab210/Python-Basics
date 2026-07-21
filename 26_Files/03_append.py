# Append to a existing file called John Doe.txt
# It should add contain data about John Doe's Hometown

f = open("John Doe.txt", "a")
string = '''
John Doe intially lived in Phoenix, Arizona. He is a very nice guy
'''
f.write(string)
f.close()