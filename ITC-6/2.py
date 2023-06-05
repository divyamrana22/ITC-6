def is_palindrome(string):
    # Convert the string to lowercase and remove whitespace
    string = string.lower().replace(" ", "")

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False



word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")