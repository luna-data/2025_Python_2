infile=open("chapter_12/11.13/phones.txt","r",encoding="utf-8") 
#인코딩 있으면 홍길동 엔터 김철수 엔터 김영희로 출력됨 -> 해결하기 위해 프린트에 엔드 설정함!
#만약 인코딩 없으면 엔드='' 이거는 필요없어요
#line=infile.readline(), readline()이 첫줄만 읽고 버려서 첫줄 출력안됨
#print(line)
for line in infile:
    line=line.rstrip()
    print(line) #,end='
infile.close()
