class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0

    def question_is_left(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        cur_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {cur_question.text} (True/False): ")
        self.check_answer(user_answer, cur_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's the  right answer")
            self.score += 1
        else:
            print("That's the wrong answer")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
