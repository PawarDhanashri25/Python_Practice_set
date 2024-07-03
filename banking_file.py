with open('banking.txt',  'r') as f:
    content=f.read().splitlines()
    w, d=0, 0 
    
    for item in content:
        tmp=item.split(':')
        print(tmp)

        if tmp[0]=='D':
            d+=int(tmp[1])
        if tmp[0]=='W':
            w+=int(tmp[1])

    net_amount=d-w
    print(net_amount)
        
