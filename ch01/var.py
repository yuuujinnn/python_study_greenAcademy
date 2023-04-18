# 변수의 선언과 사용
# 어떤 학생의 이름과 학년과 반을 출력
# 변수 이름 작성시 주의
# 숫자로 시작할수 없음, 공백을 허용하지 않음, 예약어는 쓸 수 없음
name = '이하나'

grade = 2

school_class = 1 # class는 예약어이므로 사용 불가

print(name + " 학생은" + str(grade) +" 학년 "+str(school_class)+ "반 입니다")

say = "'힘내세요.' 라고 말했습니다."
print(say)

# 문자열을 여러줄로 작성(저장)
say2 ='"python is very easy."he says.'
print(say2)

song1 = '''
        동해물과 백두산이 마르도 닳도록
        하느님이 보우하사 우리나라 만세
        '''
print(song1)


# 진수 표현하기
num = 10

b_num = 0b1010 # 이진수 표기 10
print(b_num)

h_num = 0xA # 16진수 표기법(0x 를 붙임) 
print(h_num)

# 진수 표현 함수
print(bin(10)) # 0b1010
print(bin(65))
print(hex(10))
print(chr(65)) # A
