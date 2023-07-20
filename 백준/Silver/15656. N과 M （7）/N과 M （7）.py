n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []


def dfs(start):
    if len(s) == m:
        print(*s)
        return
    # 결과가 자기 보다 큰수를 앞에 둘 수 없으니까 start ~ n 까지 반복
    for num in numbers:
        # if numbers[i] not in s:
            s.append(num)
            dfs(num)
            s.pop()


dfs(1)