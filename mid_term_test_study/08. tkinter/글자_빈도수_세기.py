string=input('문자열을 입력하시오:')
cnt_table=dict()
for letter in string:
    cnt_table[letter]=cnt_table.get(letter,0)+1

print(cnt_table)
