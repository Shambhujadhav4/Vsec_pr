string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")