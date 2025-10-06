
f = open("demo.txt", "w")  
f.write("Hello World!\n")
f.write("This is Python File Handling.\n")
f.writelines(["Welcome to Python Programming.\n", "Enjoy the Coding.\n"])
f.close()

with open ("demo1.txt","w") as file:
    file.write("Hello This is with function")


f = open("demo.txt", "r")
print("Read Entire File ")
print(f.read())    
f.close()


f = open("demo.txt", "r")
print("Read First 10 Chars")
print(f.read(10))
f.close()


f = open("demo.txt", "r")
print(" Using readline()")
print(f.readline())   
print(f.readline())   
f.close()


f = open("demo.txt", "r")
print("Using readlines() ")
lines = f.readlines()
print(lines)
f.close()


f = open("demo.txt", "a")
f.write("This line is appended.\n")
f.close()


f = open("demo.txt", "r")
print("Using tell() and seek() ")
print("Current position:", f.tell())   
print("Reading 5 chars:", f.read(5))
print("New position:", f.tell())       
f.seek(0)                              
print("After seek(0):", f.readline())  
f.close()


print("Using with statement")
with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())
