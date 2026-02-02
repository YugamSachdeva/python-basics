# Find second largest element in array

def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2]

nums = [10, 5, 20, 8, 20]
print("Second largest:", second_largest(nums))
