# List related functions

def list_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

def reverse_list(lst):
    return lst[::-1]

numbers = [1, 2, 3, 4, 5]
print(list_sum(numbers))
print(reverse_list(numbers))
