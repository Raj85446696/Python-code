def palindrome(string):
    if string == string[::-1]:
        print("it is palindrome")
    else:
        print("it is not palindrome")

palindrome("rar")