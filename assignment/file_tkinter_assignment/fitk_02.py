import os
base_dir=os.path.dirname(__file__)

filename=os.path.join(base_dir, input("텍스트 파일 이름을 입력하세요: "))

infile=open(filename,'r',encoding="utf-8")

position=0
search=input("검색 문자열을 입력하세요: ")
for line in infile:
    if search in line:
        position+=1
    else:
        pass

print(f"'{search}'(은)는 파일 내에서 {position}번 나타납니다.")
infile.close()