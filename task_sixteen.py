word = str(input("Enter a word: "))

length = len(word)

if length < 5:
    print("Short String")
elif length > 5 and len(word) < 10: 
    print("Medium String")
else:
    print("Long String")
