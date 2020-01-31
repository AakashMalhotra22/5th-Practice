class student:

    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
    def is_on_probation(self):
        if self.rank <= 3.5:
            return True
        else:
            return False

