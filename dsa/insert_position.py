# Find insert position in sorted array

def insert_position(arr, target):
    for i in range(len(arr)):
        if arr[i] >= target:
            return i
    return len(arr)

nums = [1, 2, 3, 5, 6]
target = 4

print("Insert position:", insert_position(nums, target))
