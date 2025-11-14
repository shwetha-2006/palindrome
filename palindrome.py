string = input("Enter a string: ")

# Reverse the string
rev = string[::-1]

if string == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
