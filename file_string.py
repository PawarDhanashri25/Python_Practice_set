with open('sample_file.txt') as f:
    content=f.read().splitlines()


s='\n'.join(content)

print(s)
