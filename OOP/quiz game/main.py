from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank[0].text)
# armazena uma referência ao objeto, porém pode printar o text ou answer de um objeto específico
# usa .text para acessar "text" porque question_bank[0] é uma referência da instância Question

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()
