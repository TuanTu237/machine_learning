


f = open("demo.txt", "a")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demo.txt", "r")
print(f.read())