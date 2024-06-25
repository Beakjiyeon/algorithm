N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())
import math

result = 0
for i in range(N):
    tmp = students[i] - B
    m = 0
    if tmp > 0:
        m = math.ceil(tmp / C) # 올림
    result += m + 1

print(result)
