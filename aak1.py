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
