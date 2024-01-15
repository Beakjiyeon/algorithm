import sys

N = int(input())

table = []
for _ in range(N):
    table.append([int(x) for x in sys.stdin.readline().rstrip().split()])

# 거쳐 가는 노드 k
for k in range(N):
    # 시작 노드 i
    for i in range(N):
        # 끝 노드 j
        for j in range(N):
            # i -> k , k -> j 가 연결 되어 있으면 i -> j 를 연결 되어 있다고 본다..
            if table[i][k] == 1 and table[k][j] == 1:
                table[i][j] = 1

for row in table:
    print(' '.join(map(str, row)))
