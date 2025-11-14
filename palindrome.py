import sys

print("=== Palindrome Checker ===")

# Take input from CLI or user
if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
else:
    text = input("Enter a string: ")

# Count alphabetic letters only
letters = "".join(ch.lower() for ch in text if ch.isalpha())

# Check minimum length
if len(letters) < 4:
    print("Error: Please enter at least 4 letters.")
    print("Letters found:", len(letters))
    exit()

# Palindrome check
if letters == letters[::-1]:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")