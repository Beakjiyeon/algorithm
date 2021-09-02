n = int(input()) # 번호 부른 횟수
result = [0] * 24
list = list(map(int, input().split()))

for item in list:
    result[item] = result[item] + 1

for i in range(1, len(result)):
    print(result[i], end=' ')
