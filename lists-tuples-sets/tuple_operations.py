# Tuple operations example

t = ("goa", "mumbai", "noida", "delhi")

# Access element
print(t[1])

# Convert tuple to list to modify
lst = list(t)
lst[1] = "kedarnath"
t = tuple(lst)

print(t)
