#Python Program for left and rightArray Rotation


def leftrotate(l1,d):
    for i in range(d):
        rotate_arr(l1)
def rightrotate(l2,d):
    for i in range(d):
        right_rotate(l2)
            
def rotate_arr(l):
    n=len(l1)
    temp=l1[0]
    
    for i in range(n-1):
        l1[i]=l1[i+1]

    l1[n-1]=temp

def right_rotate(l2):
    n=len(l2)
    temp=l2[n-1]
    for i in range(n-1,0,-1):
        l2[i]=l2[i-1]
    l2[0]=temp
        
    
l1=list(map(int, input().split()))
l2=list(map(int, input().split()))

d=int(input())
leftrotate(l1,d)
rightrotate(l2,d)
print(l1)
print(l2)


