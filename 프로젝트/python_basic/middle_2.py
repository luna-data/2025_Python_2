def count(word):
    global count
    count=0
    for i in word:
        if i in "aeiouAEIOU":
            count+=1
    return f"입력 문자열: {word} \n모음 개수: {count}"

a=input("문자열을 입력하세요: ")
print(count(a))