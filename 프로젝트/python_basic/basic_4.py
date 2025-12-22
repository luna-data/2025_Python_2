list1=[3,8,15,22,7,14,9,6,11,20]
new_list=[]
end_list=[]
hu_list=[]

for x in list1:
    if int(x)%2==0:
        new_list.append(x)
for y in new_list:
    end_list.append(int(y)*10)

for z in end_list:
    if int(z)>=100:
        hu_list.append(z)
sum=0
for e in hu_list:
    sum+=int(e)
print("짝수 리스트: ",new_list)
print("10 곱한 결과: ",end_list)
print("100 이상: ", hu_list)
print("합계: ",sum)
