class Course:
    def __init__(self,name):
        self.name=name
        self.scores=[]
    
    def add_score(self,s):
        self.scores.append(s)

    def avg(self):
        if len(self.scores)>0:
            return sum(self.scores)/len(self.scores)
        else:
            return 0
    
    def info(self):
        return f"과목:{self.name}, 평균:{self.avg():.1f}"

c=Course("파이썬")
c.add_score(80)
c.add_score(90)
print(c.info())
