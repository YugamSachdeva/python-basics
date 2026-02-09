# Write numbers to file
with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n40\n50\n")

# Read and calculate sum
total = 0
with open("numbers.txt") as f:
    for num in f:
        total += int(num)

print("Sum:", total)
