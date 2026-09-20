number = int(input("Enter five numebers: "))

number_one = (number // 10000) % 10
number_two = (number // 1000) % 10
number_three = (number // 100) % 10
number_four = (number // 10) % 10
number_five = (number // 1) % 10

print(number_one, number_two, number_three, number_four, number_five)
