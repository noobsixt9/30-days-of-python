from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

next_q = QuizBrain(question_bank)

while next_q.still_has_questions():
    next_q.next_question()

print("You have completed the quiz.")
print(f"Your final score is {next_q.score}/{next_q.question_number}")
