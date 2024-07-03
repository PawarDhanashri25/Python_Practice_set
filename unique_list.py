def unique_list(l):
    tmp_list=[]
    for x in l:
        if x not in tmp_list:
            tmp_list.append(x)
    return tmp_list
    

l=list(map(int, input().split(',')))
uni_list=unique_list(l)
print(list(uni_list))
