#prints the average height from given height list 
student_heights = input("Input a list of student heights ").split()
total_height = 0
for height in student_heights:
    total_height += height
    
num = 0
for n in student_heights:
    num += 1
average_height = total_height / num
print(round(average_height))
