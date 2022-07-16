#program to calculate area of circle
radius = int(input("Enter the radius of circle: "))
pi = 3.14
def area(value,value2):
  A = float((value2 * value ** 2))
  return A
print(f"Area of circle is {area(radius, pi)}")
