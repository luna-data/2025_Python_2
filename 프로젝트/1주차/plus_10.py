def problem4():
    name = ['수학', '영어', '과학', '국어']
    code = ['MT', 'EN', 'SC', 'KR']
    price = [100000, 120000, 110000, 90000]
    cnt = [0, 0, 0, 0]
    total = [0, 0, 0, 0]
    
    while True:
        code1 = input("강의 코드 입력: ")
        
        if code1 == code[0]:
            print(f"수강하신 강의는 {name[0]} 이고, 수강료는 {price[0]} 입니다.")
            cnt[0] = int(cnt[0]) + 1
            total[0] = int(total[0]) + int(price[0])
        elif code1 == code[1]:
            print(f"수강하신 강의는 {name[1]} 이고, 수강료는 {price[1]} 입니다.")
            cnt[1] = int(cnt[1]) + 1
            total[1] = int(total[1]) + int(price[1])
        elif code1 == code[2]:
            print(f"수강하신 강의는 {name[2]} 이고, 수강료는 {price[2]} 입니다.")
            cnt[2] = int(cnt[2]) + 1
            total[2] = int(total[2]) + int(price[2])
        elif code1 == code[3]:
            print(f"수강하신 강의는 {name[3]} 이고, 수강료는 {price[3]} 입니다.")
            cnt[3] = int(cnt[3]) + 1
            total[3] = int(total[3]) + int(price[3])
        elif code1 == "Q":
            break
        else:
            continue
    
    print("======================================")
    print("강의명         수강인원    총수강료")
    print("======================================")
    for i in range(4):
        if len(name[i]) == 7:
            print(f"{name[i]}  {cnt[i]}    {total[i]}")
        else:
            print(f"{name[i]}      {cnt[i]}    {total[i]}")
    print("======================================")

problem4()