def calTotal(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    return a+b+c

def sumOdd(lst):
    total=0
    for i in lst:
        if int(i)%2==0:
            total+=int(i)
    return total

def gcd(a,b,c):
    a,b,c=int(a),int(b),int(c)
    result=1
    for i in range(2,min(a,b,c)+1):
        i=int(i)
        if a%i==0 and b%i==0 and c%i==0:
            result=i
    return result

a,b,c=input("정수 3개를 입력하세요 (띄어쓰기로 구분): ").split()
lst=list(input("정수 리스트를 입력하세요(쉼표로 구분): ").split(','))
print("세 수의 합:",calTotal(a,b,c))
print("리스트 내 짝수의 합:", sumOdd(lst))
print("세 수의 최대공약수:",                                               gcd(a,b,c))