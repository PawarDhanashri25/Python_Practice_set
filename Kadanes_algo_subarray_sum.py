l=list(map(int, input().split(',')))
max_sum=0
inds=0
inde=0
for i in range(len(l)):
    s=0
    for j in range(i, len(l)):
        s=s+l[j]
        if(s>max_sum):
            max_sum=s
            inds=i
            inde=j

print(max_sum)
print(inds, inde)
print(l[inds:inde+1])


# better approach
'''
import sys

def maxSubArray(arr):
    n = len(arr)
    maxi = -sys.maxsize - 1  # Initialize to the smallest possible integer
    current_sum = 0

    start = 0
    end = 0
    temp_start = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum > maxi:
            maxi = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    sub_array = arr[start:end + 1]
    print(f"The subarray {sub_array} has the largest sum {maxi}")
    return maxi

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(arr))  # Expected output: The subarray [4, -1, 2, 1] has the largest sum 6

'''
    
    
