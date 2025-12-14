import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "phones.txt")
print(base_dir)
print(file_path)

try:
    infile = open(file_path, "r", encoding="utf-8")
    s = infile.read()
    print(s)
    infile.close()

except FileNotFoundError:
    print("오류: 파일을 찾을 수 없습니다.")

except IOError:
    print("오류: 파일을 읽는 중 문제가 발생했습니다.")
