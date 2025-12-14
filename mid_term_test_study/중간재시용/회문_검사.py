def check(s):
    low=0
    high=len(s)-1

    while True:
        if low>high:
            return True

        a=s[low]
        b=s[high]

        if a!=b:
            return False
        low+=1
        high-=1
s=input('문자열을 입력하세요: ')
s=s.replace(" ","")

if(check(s)==True):
    print('회문')
else:
    print('회문아님')