# Palindrome check

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

text = "nurses run"
print(is_palindrome(text))
