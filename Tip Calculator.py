print("Welcome to the tip calculator!")

bill_num = float(input("What was your total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))

total_cost = bill_num + tip

should_pay = total_cost / num_people


print(f'Each person should pay: ${should_pay:.2f}')

