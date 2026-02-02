# String related functions

def vowel_count(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print(vowel_count("Python Programming"))
