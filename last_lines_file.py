def tail(file,n):
    with open(file, 'r') as f:
        content=f.read().splitlines()
        l=len(content)
        tmp=content[l-n:]

    last_lines='\n'.join(tmp)
    print(last_lines)

tail('sample_file.txt', 5)
