# reversal algorithm for array rotation

'''
#Rotate the array to the left by 'd' 
arr=[1,2,3,4,5]
d=int(input())
c=(arr[d:]) +(arr[:d])
print(c)

'''

def reverse_arr(arr):
    start=0
    end=len(arr)-1
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1


arr=list(map(int, input().split()))

d=int(input())

reverse_arr(arr)
print(arr)




