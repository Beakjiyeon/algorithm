# https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-9465-%EC%8A%A4%ED%8B%B0%EC%BB%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))
