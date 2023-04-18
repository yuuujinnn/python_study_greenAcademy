'''
# 입력처리 - input()함수
print("이름을 입력해 주세요")
name = input() # 문자를 입력할 수 있음
print(name + "님 환영해요!!")

# 방법2
name = input("이름을 입력해 주세요 \n")
print(name)

# 입력받은 수는 문자열임 -> 정수로 변환 int() 함수 사용
number = int(input("숫자를 입력해 주세요(1~10) " ))
print(number * 2)

# 두 수를 입력받아 합을 계산하기
x = int(input("첫째 수 입력 : "))
x = int(input("두번째 수 입력 : "))

sum_v = x + y
print(sum_v)


# 나이 계산 프로그램
# 나이 = 현재년도 - 출생년도 + 1
# 태어난 년도를 입력해 주세요
current_year = 2023
birth_year = int(input("태어난 년도를 입력해 주세요. "))

age = current_year - birth_year +1

print(str(age) + "세")
'''
# 사각형의 넓이를 계산하는 프로그램 작성

x = int(input("가로의 길이 입력 "))
y = int(input("세로의 길이 입력 "))

result = (x * y)
print("가로 길이 : "+str(x)+"cm")
print("세로 길이 : "+str(y)+"cm")
print("넓이 : " +str(result)+"cm")
