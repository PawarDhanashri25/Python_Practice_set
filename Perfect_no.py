def perfect_no(n):
    s=0
    for i in range(1, (n//2)+1 ):
        if n%i==0:
            s+=i
    
    if(n==s):
        return True
    else:
        return False

no=int(input())

result=perfect_no(no)

if(result):
    print(f"{no} is perfect number")
else:
    print(f"{no} is not perfect number")
    
            
