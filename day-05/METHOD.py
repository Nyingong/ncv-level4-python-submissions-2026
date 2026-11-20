class Learner:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.marks = []
   
    def add_mark(self, mark):
        self.marks.append(mark)
   
    def average(self):
        total = 0
        for m in self.marks:
            total = total + m
        return total / len(self.marks)
 
thandi = Learner("2024001", "Thandi")
thandi.add_mark(65)
thandi.add_mark(72)
thandi.add_mark(58)
print(thandi.marks)
print(thandi.average())
