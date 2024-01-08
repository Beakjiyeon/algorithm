n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

count = 0
left = k
for coin in coins:
    # 몫
    count += left // coin
    # 나머지
    left = left % coin
print(count)
