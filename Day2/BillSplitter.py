#Day 2 final project 
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip_percent = int(input("How much tip would you like yo give? 10, 12, or 15? "))
split = int(input("How many peope to split the bill? "))
tip_amount = ((bill * tip_percent) / 100) / 5
result = (bill / split) + tip_amount
print(f"Each person should pay ${round(result,2)}")
