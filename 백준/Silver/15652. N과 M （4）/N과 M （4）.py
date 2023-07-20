
n, m = map(int, input().split())
s = []
def dfs(start):
    # print(f"### dfs({start})")
    if len(s) == m:
        print(*s)
        return
    # print("### for", start, "~", n)
    # 숫자를 중복하여 뽑을 수 있으니까 1 ~ n 까지 한 사이클 크게 반복
    for i in range(start, n + 1):
        s.append(i)
        # 길이 m개 결과를 얻을 때 까지 반복
        dfs(i)
        # 길이 m개 결과를 내고 난 뒤 pop 하여 다음 반복 분기로 이동
        # 큰 반복 사이클(1~4), 작은 세부 반복 사이클 (1~4), (2~4), (3~4), (4~4) 진행됨
        s.pop()
dfs(1)