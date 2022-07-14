#add even number between 1 to 100 and prints out the total result
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)
