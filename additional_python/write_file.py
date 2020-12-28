newFile = open('new_file.txt', 'w+')
string = "this is a dummy text, \nhabba habba"
newFile.write(string)
newFile.close()

f = open("new_file.txt", "r")
print(f.read())
f.close()
