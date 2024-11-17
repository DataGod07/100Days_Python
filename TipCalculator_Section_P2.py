# Tip Calculator
print('Welcome to tip calculator! ')
bill = float(input("What was the total bill? $"))
tip = int(input('How much would you like to tip? 10, 12, or 15? '))
total_people = int(input('How many people to split the bill ? '))
total_bill = 0
if tip == 10:
    total_bill = float((bill + bill * 10 / 100) / total_people)
if tip == 15:
    total_bill = float((bill + bill * 15 / 100) / total_people)
if tip == 12:
    total_bill = float((bill + bill * 12 / 100) / total_people)
print(f'Each person should pay: ${round(total_bill, 2)}')
