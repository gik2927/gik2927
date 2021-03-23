from random import *

tt = range(1,5)
tt = list(range(1,5))
shuffle(tt)
tt2 = sample(tt,1)
print("발모제를 찾아라!")
#print("{0}".format(tt2))
me = sample(tt ,2)
me1 = randint(1,4)#me[0]
me2 = randint(1,4)#me[1]

for i in range(1,4):
    print("약 {0}과 {1}을 바릅니다".format(me1, me2))
    me1 = randint(1,4)#me[0]
    me2 = randint(1,4)#me[1]
    if me1 == tt2 or me2 == tt2:
        print("머리가 자랐습니다")
    else:
        print("머리가 자라지 않았습니다")
answer = int(input("그렇다면 발모제는 몇번?"))
if answer == tt2:
    print("정답입니다")
else:
    print("아닙니다{0}".format(tt2))
