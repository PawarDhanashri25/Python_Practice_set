import time
def tail(file,n):
    with open(file, 'r') as f:
        content=f.read().splitlines()
        l=len(content)
        tmp=content[l-n:]

    last_lines='\n'.join(tmp)
    return last_lines

while True:
    s=tail('sample_file.txt', 5)
    print(s)
    time.sleep(3)
    print(' ') 
