import os
base_dir=os.path.dirname(__file__)

filename=os.path.join(base_dir, input("텍스트 파일 이름을 입력하세요: "))

with open(filename,'rb')as file:
    search=input("검색 문자열을 입력하세요: ")
    file.seek(search)

    position=file.tell()
    print(f"'{search}'(은)는 파일 내에서 {position}번 나타납니다.")

    data=file.read(5)
    print("잃은 데이터:",data)