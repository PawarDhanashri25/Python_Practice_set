with open ('macs.txt') as f:
    content=f.read().split()
    content=list(set(content))
    
with open('mac_unique.txt', 'a', newline='') as f1:
    for mac in content:
        f1.write(f"{mac}\n")
        



    

    
