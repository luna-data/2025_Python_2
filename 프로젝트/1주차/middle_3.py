num_list=[]
num_dict={}
a=input("입력: ").split(',')
for i in a:
    if 90<=int(i)<=100:
        grade="A"

    elif 80<=int(i)<90:
        grade="B"

    elif 70<=int(i)<80:
        grade="C"
    
    elif 60<=int(i)<70:
        grade="D"
    else:
        grade="F"

    num_dict[grade]=

