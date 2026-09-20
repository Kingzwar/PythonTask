word = str(input("Enter a word: "))

first_character = word[0]
last_character = word[-1]

if first_character == last_character:
        print("It is palindrome")
else:
        print("It is not palindrome")
