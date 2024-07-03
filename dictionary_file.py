with open('american-english.txt') as f:
    content=f.read().splitlines()

    di=dict()
    
    
    for item in content:
        di[item]=len(item)

    print(di)
    
        
