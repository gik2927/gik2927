from random import *

aicard = randint(1,5)
rccard = 4
print("--------------e-card----------------")
print("----------모드를 정해주세요.---------")
for i in range(0,9999):
    modselect = int(input("     1:혼자 2:온라인 3:하는 방법"))
    if modselect == 1:
        print("         그럼 시작합니다")
        break
    elif modselect == 2:
        print("         준비중 입니다")
        continue
    elif modselect == 3:
        print("")
        continue
    else:
        print("         다시 선택해주세요")
        continue


print("---------카드를 정해 주세요.---------")

for x in range(0,111111111):
    cardselect = int(input("------------1:황제--2:노예-----------"))
    if cardselect ==1:
        
        print("------당신의 선택을 황제입니다------")
        break
    if cardselect ==2:
        print("---------준비중입니다---------")
        continue
for e in range(0,99):
    yc = int(input("카드를 골라주세요 1:시민카드 2:황제카드 \n 남은 시민카드[{0}장]".format(aicard)))
    aicard = randint(1,5)
    if yc == 1:   
        print("당신은 시민 카드를 내셨습니다")
        rccard -= 1    
        if aicard == 1:
            battlecard = "노예"
            print("상대방이 카드를 고르고 있습니다")
            print("오픈합니다")
            print("상대가 고른 노예카드 VS 당신이 고른 시민카드")
            print("따라서 당신의 승리!")
            break
        else:
            battlecard = "시민"
            print("상대방이 카드를 고르고 있습니다")
            print("오픈합니다")
            print("상대가 고른 시민카드 VS 당신이 고른 시민카드")
            print("무승부 다시 카드를 내세요!")
            aicard = randint(1,5)
        if rccard ==0:
            print("모든 시민카드를 내셨습니다. 당신의 패배")
            break
    if yc == 2:
        battlecard2 = "황제"
        print("당신은 황제 카드를 내셨습니다")  
        if rccard ==0:
            print("당신의 패배")
            break    
        if aicard == 1 or 3:
            battlecard = "노예"
            print("상대방이 카드를 고르고 있습니다")
            print("오픈합니다")
            print("상대가 고른 노예카드 VS 당신이 고른 황제카드")
            print("당신의 패배")
            break
        else:
            battlecard = "시민"
            print("상대방이 카드를 고르고 있습니다")
            print("오픈합니다")
            print("상대가 고른 시민카드 VS 당신이 고른 황제카드")
            print("당신의 승리!")
            break
if rccard ==0:
    print("끝났습니다 당신의 패배입니다")