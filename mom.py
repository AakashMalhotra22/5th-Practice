import mcq
from test1 import love
from test1 import love
prompt = [
    "Why?\n(a) son \n(b) family\n\n",
    "What?\n(a) son \n(b) family\n\n"

]


questions = [

    love(prompt[0], "a"),
    love(prompt[1], "b")

]

def run_test(questions):
    score = 0
    for question in questions:
      answer = input(question.parshan)
    if answer == question.answer:
           score += 1
    print("You got "+ str(score) +"/" + str(len(questions)) + "correct.")

run_test(questions)


print(mcq.aakash(questions))