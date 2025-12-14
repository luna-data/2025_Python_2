time=int(input("초를 입력해주세요: "))
hour=time//3600
min=(time-3600*hour)//60
sec=(time-hour*3600-min)//60
print(f"{time}초는 {hour}시간 {min}분 {sec}초 입니다.")