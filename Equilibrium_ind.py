def equilibrium(arr):
    n=len(arr)
    
    
    for i in range(n):
        leftsum=0
        rightsum=0
        
        for j in range(i):
            leftsum+=arr[j]
        
        for j in range(i+1, n):
            rightsum+=arr[j]
        
        if(leftsum==rightsum):
            return i
        
    return -1
    
    
    
if __name__=="__main__":
    arr=list(map(int, input().split(',')))
    ind=equilibrium(arr)
    print("Equilibrium index is: ", ind)
    
    
