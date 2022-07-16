numbers = input("enter numbers: ").split()
def greatest(num):
    maxi = numbers[0]
  
    for i in numbers:
       if i > maxi:
           maxi = i
    return maxi
print(f"Greatest number is {greatest(numbers)}")
