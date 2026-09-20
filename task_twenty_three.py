first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second number: "))
third_number = int(input("Enter Third number: "))

largest = first_number

if second_number > largest: 
        largest = second_number

if third_number > largest:
        largest = third_number
print(largest)
