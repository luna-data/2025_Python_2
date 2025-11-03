class Course:
    def __init__(self,name):
        self.name=name
        self.scores=[]
    
    def add_score(self,s):
        self.scores.append(s)

    def avg(self):
        return sum(self.scores)/len(self.scores)
    
    def info(self):
        print(str((f"과목:{self.name}, 평균:{self.avg()}")))

c=Course("파이썬")
c.add_score(80)
c.add_score(90)
print(c.info())
