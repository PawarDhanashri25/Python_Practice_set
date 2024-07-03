with open('fi1.txt', 'r') as f:
    content1=f.read().splitlines()


with open('fi2.txt', 'r') as f1:
    content2=f1.read().splitlines()

file=list(zip(content1, content2))

#print(file)

i=0
for item in file:
    i+=1
    if (item[0]!=item[1]):
        print(f"file 1: {item[0]}\nfile 2: {item[1]} ")
