from test import ram

prompt = [
    "1. Who is the president of India\n(a) N \n(b) M\n\n",
    "2. Who is Aakash\n(a) P\n (b) G\n\n"


]

questions = [
    ram(prompt[0], "a"),
    ram(prompt[1],"b")

]

def aakash(questions):
    score = 0
    for question in questions:
       answer = input(question.parshan)
       if answer == question.answer:
           score += 1
    print("You got " + str(score) + "/" +str(len(questions)) + "correct" )


aakash(questions)




