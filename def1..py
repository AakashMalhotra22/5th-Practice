def cube(num):
    return num*num*num

print(cube(3))

class Mathematicians:
    def __init__(self, name, college, score_in_maths):
        self.name = name
        self.college = college
        self.score_in_maths = score_in_maths

    def on_honor_role(self):
        if self.score_in_maths <= 15:
            return "good"
        if self.score_in_maths >= 15:
            return "excellent"

Student1 = Mathematicians("ram", "r", 15)
print(Student1.on_honor_role())

class teacher:

    def teach_maths(self):
        print("He can teach maths.")
    def teach_chemistry(self):
        print("He can teach chemisty")
    def teach_arts(self):
        print("He can teach arts")

Student2 = teacher()
(Student2.teach_chemistry())