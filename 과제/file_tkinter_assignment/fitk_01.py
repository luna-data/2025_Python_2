import os
base_dir=os.path.dirname(__file__)
filename=input("텍스트 파일 이름을 입력하세요: ").strip()
filepath=os.path.join(base_dir, filename)
infile=open(filepath, "r",encoding="utf-8")

try:
    with open("infile",'r') as file:
        content=file.read()
    print(content)

except FileNotFoundError:
    print("파일을 찾을 수 없습니다!")

finally:
    print("파일 처리 완료.")


