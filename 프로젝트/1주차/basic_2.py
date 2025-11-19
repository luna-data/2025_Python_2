score=[85,92,78,45,90]
count=0
new_list=[]

for i in score:
    if int(i) >=60:
        count+=1
        new_list.append(i)
    avg=sum(score)/5
    max_num=max(score)
    min_num=min(score)

print('예시입력 : ',score)
print('60점 이상:',count)
print('평균:',avg)
print('최고점:',max_num,'최저점:',min_num)
print('평균 이상 점수:',new_list)