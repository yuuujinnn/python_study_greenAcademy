# 집합 - set(), {}를 사용
# 순서가 없다, 중복 허용 안됨
s = {2, 4, 6, 8}

# 요소 추가
s.add(10)

# 요소 삭제
s.remove(4)

print(2 in s)
print(3 in s)

# 전체 삭제
s.clear()

# 전체 조회
for i in s:
    print(i)

print(s)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# 교집합(A&B), 합집합(A|B), 차집합(A-B)
print(A & B)
print(A | B)
print(A - B)

# 자료 중복 제거
a = [1, 1, 1, 2, 2, 3]
s = set(a)
print(s)
# 리스트로 변환
print(list(s))

say = set('Hello')
print(say)