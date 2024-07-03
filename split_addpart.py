#Python Program to Split the array and add the first part to the end

'''
# first appraoch 
def splitarr(arr,s):

    c=(arr[s:])+(arr[:s])
    return c 
'''

#second appraoch 
def split_arr(arr, s):
    n=len(arr)
    for i in range(s):
        temp=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=temp
    

arr=[12,10,5,6,52,36]
s=int(input())
'''
result=splitarr(arr,s)
print(result)
'''

split_arr(arr,s)
print(arr)

