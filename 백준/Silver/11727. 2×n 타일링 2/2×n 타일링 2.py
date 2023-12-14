def solution():
    n = int(input())
    if n == 1: # https://www.acmicpc.net/board/view/34270
        print(1) 
        return 0
    dp = [0] * (n + 1)  # dp[0] 은 비워 둠
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1):  # dp[3] ~ dp[n] 값 구하기
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    print(dp[n] % 10007)


if __name__ == '__main__':
    solution()