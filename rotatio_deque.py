from collections import deque

def rotate_array_deque(arr, d):
    n = len(arr)
    rotated_array = deque(arr)
    rotated_array.rotate(-d)    # for rotate the array in left 
    return list(rotated_array)

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

rotated_array = rotate_array_deque(arr, d)
print("Rotated array:", rotated_array)


rotated_array.rotate(d)  # rotate the array in right 
