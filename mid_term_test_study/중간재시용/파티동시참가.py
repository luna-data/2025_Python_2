A=input('A: ')
B=input('B: ')

partyA=set()
partyB=set()

for s in A.split():
    partyA.add(s)

for s in B.split():
    partyB.add(s)

print(partyA|partyB) #우클릭해서 실행하기!!