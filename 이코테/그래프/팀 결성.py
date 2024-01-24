n, m = map(int, input().split())


# 팀 합치기 : 부모 노드 통일
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    # 최종 루트 부모로 비교
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_same_team(a, b):
    if find_parent(a) == find_parent(b):
        return True
    else:
        return False


parent = [i for i in range(0, n + 1)]
for _ in range(m):
    type, a, b = map(int, input().split())
    if type == 0:
        union(a, b)
    elif type == 1:
        if is_same_team(a, b):
            print('YES')
        else:
            print('NO')

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
