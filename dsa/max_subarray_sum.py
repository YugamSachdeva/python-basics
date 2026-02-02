# Maximum Subarray Sum (Kadane's Algorithm)

def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

nums = [1, 2, 3, -2, 5]
print(max_subarray_sum(nums))
