outfile=open("sample.bin","wb")

data_to_write=bytes([255,128,0,1,10,50])

outfile.write(data_to_write)
outfile.close()
print("sample.bin 파일에 바이트 데이터를 저장했습니다.\n")

infile=open("sample.bin","rb")
bytesArray=infile.read()
infile.close()

print("읽어온 bytesArray:", bytesArray)
print("타입:", type(bytesArray))

print("\n개별 바이트 값 출력:")
for i,b in enumerate(bytesArray):
    print(f"{i}번째 바이트 =",b)