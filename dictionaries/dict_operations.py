# Dictionary operations example

marks = {
    "eng": 56,
    "maths": 96,
    "hindi": 89
}

# Calculate average
total = sum(marks.values())
avg = total / len(marks)
print("Average:", avg)

# Find subject with highest marks
max_subject = max(marks, key=marks.get)
print("Highest marks in:", max_subject)
