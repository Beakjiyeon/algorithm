n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []


def dfs(start):
    if len(s) == m:
        print(*s)
        return
    # 결과가 자기 보다 큰수를 앞에 둘 수 없으니까 start ~ n 까지 반복
    for i in range(start, n):
        s.append(numbers[i])
        dfs(i)
        s.pop()


dfs(0)