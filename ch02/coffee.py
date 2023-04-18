# 연습문제
# 커피 자동판매기 프로그램

# 돈을 입력하면 커피가 나온다. (커피 가격 : 400원)
# 돈이 커피 가격을 초과하면 거스름돈을 돌려준다.
# 돈이 커피 가격보다 작으면 돈은 돌려주고 커피가 나오지 않는다.
# 커피의 수량이 소진되면 판매가 중지된다 (커피 수량 : 5개)

coffee = 5

while True:
    try:
        money = int(input("돈을 넣어주세요 : "))
        
        if money == 400:
            print("커피가 나옵니다.")
            coffee -= 1    # coffee = coffee -1
        elif money > 400:
            print(f'커피가 나오고, 거스름돈 {money-400}원을 돌려 받습니다.')
            coffee -= 1
        else:
            print("커피가 나오지 않습니다.")
        print(f'남은 커피의 양은 {coffee}개 입니다.')

        if coffee == 0:
            print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
            break
    except:
        pass
