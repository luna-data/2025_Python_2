import os
base_dir=os.path.dirname(__file__)

filename=os.path.join(base_dir, input("텍스트 파일 이름을 입력하세요: "))

try:
    with open(filename,'r',encoding="utf-8") as file:
        content=file.read()
        print(content)
        file.close()

except FileNotFoundError:
    print("파일을 찾을 수 없습니다!")
