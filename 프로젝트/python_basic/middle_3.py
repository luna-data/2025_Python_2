num_list=[]
num_dict={}

num=input("입력: ").split(',')
for i in num:
    if 90<=int(i)<=100:
        grade="A"
        num_dict[grade]=num_dict.get(grade,0)+1
    elif 80<=int(i)<90:
        grade="B"
        num_dict[grade]=num_dict.get(grade,0)+1

    elif 70<=int(i)<80:
        grade="C"
        num_dict[grade]=num_dict.get(grade,0)+1
    elif 60<=int(i)<70:
        grade="D"
        num_dict[grade]=num_dict.get(grade,0)+1
    else:
        grade="F"
        num_dict[grade]=num_dict.get(grade,0)+1
num_dict= dict(sorted(num_dict.items()))
print(num_dict)