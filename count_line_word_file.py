def count_fun(file):
    with open(file) as f:
        
        content=f.read().splitlines()
        l=len(content)
        word=0
        for line in content:
            word+=len(line.split())
        chars=0
        for line in content:
            chars+=len(list(line))
            
            
    return l, word, chars





l, w, c=count_fun('sample_file.txt')
print(l, w, c)
