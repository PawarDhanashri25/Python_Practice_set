with open('file.txt') as f:
    content=f.readlines()

    temp_list=[line for line in content if line.strip() !='']

    print(temp_list)

with open('file2.txt' , 'w' ) as f:
    f.write(''.join(temp_list))
