from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
lost = False
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.question_is_left():
    quiz.next_question()

print("You have Completed the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
