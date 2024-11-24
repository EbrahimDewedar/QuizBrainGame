
# from data import question_data
# from question_model import Question
# from quiz_brain import QuizBrain
#
# question_bank = []
# for item in question_data:
#     the_question = item["text"]
#     the_answer = item["answer"]
#     new_question = Question(the_question, the_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
# while quiz.still_has_question():
#     quiz.next_question()


# from data import question_data
# from question_model import Question
# from quiz_brain import QuizBrain
#
# question_bank = []
# for item in question_data:
#     the_question = item["text"]
#     the_answer = item["answer"]
#     new_question = Question(q_text = the_question, q_answer = the_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
# while quiz.still_has_question():
#     quiz.next_question()
#
# print("you've completed the Quiz")
# print(f"your final score was {quiz.score}/{quiz.question_number}")
# print(f"your final score was {quiz.score}/{len(question_bank)}")

# from data import question_data
# from question_model import Question
# from quiz_brain import QuizBrain
#
# question_bank = []
# for item in question_data:
#     the_question = item["text"]
#     the_answer = item["answer"]
#     new_question = Question(the_question, the_answer)
#     question_bank.append(new_question)
#
# final_quiz = QuizBrain(question_bank)
# while final_quiz.still_have_question():
#     final_quiz.next_question()
#
# print("you've completed the quiz.")
# print(f"your score was {final_quiz.score}/{final_quiz.question_number}")

from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []
for item in question_data:
    the_question = item["text"]
    the_answer = item["answer"]
    new_question = Question(the_question, the_answer)
    question_bank.append(new_question)

final_quiz = QuizBrain(question_bank)
while final_quiz.still_has_question():
    final_quiz.next_question()

print("you have completed the quiz")
print(f"your final score was {final_quiz.score}/{final_quiz.question_number}")

















