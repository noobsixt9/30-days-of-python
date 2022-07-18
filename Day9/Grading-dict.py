
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

for scores in student_scores:
    score = student_scores[scores] 
    if score >= 91 and score <= 100:
        remark = "Outstanding"
        student_grades[scores] = remark
    elif score >= 81 and score <= 90:
        remark = "Exceeds Expectations"
        student_grades[scores] = remark
    elif score >= 71 and score <= 80:
        remark = "Acceptable"
        student_grades[scores] = remark
    elif score <= 70:
        remark = "Fail"
        student_grades[scores] = remark
        
print(student_grades)
