n, m = map(int, input().split())
numbers = sorted([int(x) for x in input().split()])
s = []


def dfs(start):
    if len(s) == m:
        print(*s)
        return
    # 1 ~ n 까지 크게 반복
    for num in numbers:
        # 결과에 중복을 허용하지 않으므로
        if num in s:
            continue
        s.append(num)
        dfs(start)
        s.pop()


dfs(1)