with open("practice.txt", "r") as f:
    #f.write("Hi everyone\nWe are learning file I/O]\n")
    #f.write("using Java.\nI like programming language Java.")

    content=f.read()

    content=content.replace("Java", "Python")
    print(content)

    
