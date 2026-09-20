principal = int(10000)
rate = float(0.07)
ten_years = int(10)
twenty_years = int(20)
thirty_years = int(30)

year_one = principal * (1 + rate)** ten_years
year_two = principal * (1 + rate)** twenty_years
year_three = principal * (1 + rate)** thirty_years

print("10 years: $", year_one)
print("20 years: $", year_two)
print("30 years: $", year_three)

