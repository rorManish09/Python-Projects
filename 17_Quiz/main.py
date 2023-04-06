from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:

    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():

    quiz.next_question()

print("You've have completed the quiz")

print(f"Your final score was: 10/{len(question_bank)}")