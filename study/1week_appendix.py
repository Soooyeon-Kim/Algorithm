# 수 자료형 & 연산
# 10억 지수 표현 방식
a = 1e9
print(a) 

# output : 1000000000.0

# 752.5
b = 75.25e1
print(b)

# output : 752.5

# 3.954
c = 3954e-3
print(c)

# output : 3.954

d = 0.3 + 0.6
print(d)

# output : 0.8999999999999999

if d == 0.9:
	print(True)
print(False)

# output : False

print(round(d, 4))

# output : 0.9

if d == 0.9:
	print(True)
print(False)

# output : True

a = 7
b = 3

# 나누기 
print(a/b)

# 나머지
print(a%b)

# 몫
print(a//b)

'''output :
2.3333333333333335
1
2
'''

# 2  List Comprehension
li = list(range(1, 10, 1))
''' another
import numpy as np
np.arange(1, 10, 1)
'''
print(li)

# output : [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(0,20) if i%2 ==1]
print(array)

# output : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 0부터 19까지의 수 중에서 제곱 값을 포함하는 리스트
array = [i*i for i in range(0,20)]
print(array)

# output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]


# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# output : [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

'''
언더바(_)의 역할? 
파이썬 자료구조/ 알고리즘에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_) 를 사용한다.
'''
# ex 
summary = 0 
for i in range(1,10) : 
	summary += 1
	print(summary)


''' output :
1
2
3
4
5
6
7
8
9 '''

# ex
for _ in range(5):
    print("Hello World!") 

''' output :
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
'''

# 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야 한다. 
# 먄약 NxM 크기의 2차원 리스트를 초기화한다면, 의도하지 않은 결과가 도출될 수 있다.

# 리스트 관련 메서드
a = [1,4,7,9,11]
a.reverse()
print(a) 

# output : [11, 9, 7, 4, 1]

# 특정 인덱스에 데이터 추가
a.insert(2,3)
print(f'2 인덱스에 3 추가 : {a}')

# output : 2 인덱스에 3 추가 : [11, 9, 3, 7, 4, 1]

# 특정 값인 데이터 개수 세기
print(f'값이 3인 데이터 개수 : {a.count(3)}')

# output : 값이 3인 데이터 개수 : 1

result = [ i for i in li if i not in remove_set]
print(result)

# output : [1, 2, 7, 8, 8]

# 딕셔너리 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['포도'] = 'Grape'

# 키 데이터만 담은 리스트
fruit_list = data.keys()

# 값 데이터만 담은 리스트
fruit_list2 = data.values()

print(fruit_list)

print(fruit_list2)

''' output :
dict_keys(['사과', '바나나', '포도'])
dict_values(['Apple', 'Banana', 'Grape'])
'''

# 집합 자료형 초기화 1
data = set([1,2,3,3,3,3,4,5,6,8,8,8])
print(data)

# output : {1, 2, 3, 4, 5, 6, 8}

# 집합 자료형 초기화 2
data = {1,2,3,3,3,3,4,5,6,8,8,8}
print(data)

# output : {1, 2, 3, 4, 5, 6, 8}

# 집합 자료형 연산
aset = set([1,2,3,4,5])
bset = set([3,4,5,6,7])

print(aset | bset) # 합집합
print(aset & bset) # 교집합
print(aset - bset) # 차집합

''' output :
{1, 2, 3, 4, 5, 6, 7}
{3, 4, 5}
{1, 2}
'''

# 집합 자료형 함수
# 새로운 원소 추가
data.add(9)
print(data)

# output : {1, 2, 3, 4, 5, 6, 8, 9}

# 새로운 원소 여러 개 추가
data.update([10,11,12])
print(data)

# output : {1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12}

# 특정한 값을 갖는 원소 삭제
data.remove(6)
print(data)

# output : {1, 2, 3, 4, 5, 8, 9, 10, 11, 12}