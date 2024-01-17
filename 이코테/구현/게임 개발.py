# 행, 열
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵
d = [[0] * m for _ in range(n)]

# 캐릭터의 현재 x, y 좌표, 방향
x, y, direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전하는 함수 : 작은 단위로 나누자
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 1. 왼쪽으로 회전
    turn_left()
    # 2. 해당 방향으로 전진
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 2-1. 가보지 않은 칸이 존재하는 경우 이동함
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        turn_time = 0
        d[nx][ny] = 1
        continue
    # 2-2. 가보지 않은 칸이 없거나 바다인 경우 이동 안함
    else:
        turn_time += 1

    # 3. 네 방향으로 모두 갈 수 없는 경우 한칸 뒤로 이동
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동함
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤로 갈 수 없다면(바다) 이동 종료
        else:
            break
        turn_time = 0

print(count)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

'''
* 문제 이해 어려웠으나 의외로 꼬지 않은 로직이었다.
* 작은 단위 turn_left()를 함수화 한다.
* 방향 회전 횟수 변수를 두고, 모든 방향을 돌아도 안나오는 경우엔 turn_time 한다.
* 방문 안했고, 육지인지 체크
'''
