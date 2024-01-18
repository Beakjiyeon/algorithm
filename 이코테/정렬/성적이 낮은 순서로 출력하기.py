n = int(input())

arr = []
for _ in range(n):
    student, score = input().split()
    arr.append((student, int(score)))

arr.sort(key=lambda element: element[1])

for element in arr:
    print(element[0], end=' ')

'''
튜플은 값을 바꿀 수 없다.

정렬
lambda 원소 : 기준 값
2
홍길동 95
이순신 77
'''
