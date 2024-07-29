N = int(input())
K = int(input())
apples = [tuple(map(int, input().split(' '))) for _ in range(K)] # 리스트 to 튜플
L = int(input())

points = []
directs = []
for _ in range(L):
    m = input().split(' ')
    points.append(int(m[0])) # 게임 시작 기준이라 누적 안함
    directs.append(m[1])

time = 0
cx, cy = 1, 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cd = 0
body = [(1, 1)]

while True:
    if time in points:
        idx = points.index(time)
        cd_en = directs[idx]
        if cd_en == "D":
            cd += 1
            if cd == 4:
                cd = 0
        else:
            cd -= 1
            if cd == -1:
                cd = 3
    time += 1
    nx, ny = cx + dx[cd], cy + dy[cd]
    if 1 <= nx <= N and 1 <= ny <= N and (nx, ny) not in body:
        body.append((nx, ny))
        cx, cy = nx, ny
        if (cx, cy) not in apples:
            body.pop(0)
        else:
            # 사과를 먹고 나서, 먹었다 처리 필요
            apples.remove((cx, cy))
    else:
        break
print(time)
