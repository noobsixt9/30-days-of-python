from replit import clear
from art import logo
def calculator():
  print(logo)
  def add(x, y):
    """"This fuction takes 2 number and gives their sum"""
    sum = x + y
    return sum
  def subtract(x, y):
    """"This fuction takes 2 number and gives their subtraction"""
    sub = x - y
    return sub
  def multiply(x, y):
    """"This fuction takes 2 number and gives their multiplication"""
    mul = x * y
    return mul
  def divide(x, y):
    """"This fuction takes 2 number and gives their division"""
    div = x / y
    return div
  
  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }
  
  num1 = float(input("What's the first number?: "))
  continue_program = True 
  while continue_program: 
    for operation in operations:
      print(operation)
    choose = input("Choose your operator: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[choose]
    answer = calculation_function(num1,num2)
    print(f"{num1} {choose} {num2} = {answer}")
    cont = input(f"Type 'y' to contiue calculating with {answer} or type 'n' to start new calculation or type 'exit' to exit program: ")
    if cont == "y":
      num1 = answer
    elif cont == "n":
      continue_program = False
      clear()
      calculator()
    elif cont == "exit":
       continue_program = False
calculator()
