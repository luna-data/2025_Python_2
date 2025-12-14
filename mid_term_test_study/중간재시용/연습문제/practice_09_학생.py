class Student:
    def __init__(self, name):
        self.name=name
        self.score=[]

    def add_score(self,score):
        self.score.append(self.score)
        print(f"{self.name}의 성적 {score}점이 추가되었습니다.")

    def cal_avg(self):
        if not self.score: #없는 경우도 대비해서 0을 반환하는 부분 생성
            return 0
        return sum(self.score)/len(self.score) #평균 연산
    
student=Student("Kim")

student.add_score(90)
student.add_score(85)
student.add_score(78)

avg=student.cal_avg()
print(f"{student.name}의 평균 성적: {avg:.2f}")