#basic fizzbuzz game in which it prints FizzBuzz when the number is exactly divisible by 3 and 5, Fizz when number is exactly divisible by 3 and Buzz when
#number is divisible by 5
for i in  range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
