import math
def paint_calc(height, width, coverage):
  number_of_cans = (height * width) / coverage
  print(f"You'll need to buy {math.ceil(number_of_cans)}")
  
cover = 5
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

paint_calc(height=test_h, width=test_w, coverage=cover)
