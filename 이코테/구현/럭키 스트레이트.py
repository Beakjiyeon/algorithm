''' 
내 풀이
scores = list(map(int, list(input())))

pivot = len(scores) // 2

left = sum(scores[:pivot])
right = sum(scores[pivot:])

print("LUCKY" if left == right else "READY")
'''

# 변수 감소
n = input()
length = len(n)
sum = 0
# 왼쪽 자리 수 합
for i in range(length // 2):
    sum += int(n[i])

# 오른쪽 자리 수 합
for i in range(length // 2, length):
    sum -= int(n[i])

print("READY" if sum else "LUCKY")
