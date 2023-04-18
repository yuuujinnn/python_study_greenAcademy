# while 반복문
# 'hello'를 10번 출력
'''
i = 1
while i <= 10:
    print( 'hello~', i )
    i += 1
'''

# 1부터 10까지 더하기
'''
i = 0
sum_v = 0
while i < 10:
    i += 1
    sum_v = sum_v + i
    print(i)

print(f'합계 : {sum_v}')
'''

# 반복 조건문(break)
'''
i = 0
sum_v = 0
while True:
    i += 1
    if i > 10 :
        break  
    sum_v += i  
    print( f' i = {i}, sum_v = {sum_v}')
    
print(f'합계 : {sum_v}')
'''


# 반복문 연습
# 'y'를 입력하면 '반복 계속' 'n'을 입력하면 '반복 중단' 그외 '정상 답변이 아님' 
while True:
    answer = input("반복을 계속 할까요?(y/n)")
    
    if answer == 'y' or answer == 'Y':
        print("반복을 계속 합니다.")
    elif answer == 'n' or answer == 'N':
        print("반복을 중단 합니다.")
        break
    else:
        print("정상 답변이 아닙니다.")
