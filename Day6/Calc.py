#simple calulator machine using functions and conditions
number1 = int(input("Enter first number: "))
number2 = int(input("Enter first number: "))
print("\n 1 for addition \n 2 for substraction \n 3 for multiplication \n 4 for division\n")
opt = int(input("Choose option: "))

def add(x, y):
  sum = x + y
  return sum
def minus(x, y):
  sub = x - y
  return sub
def mul(x, y):
   multi = x * y
   return multi
def div(x, y):
  division = x / y
  return division
if opt == 1:
  print(f"\nAddition = {add(number1, number2)}")
if opt == 2:
  print(f"\nSubtraction = {minus(number1, number2)}")
if opt == 3:
  print(f"\nMultiplication = {mul(number1, number2)}")
if opt == 4:
  print(f"\nDivision = {div(number1, number2)}")
