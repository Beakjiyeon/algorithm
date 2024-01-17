location = input()
cols = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

# 열
# x = cols[location[0]]
# ord('a') : 97 유니 코드 정수 반환
x = int(ord(location[0])) - int(ord('a')) + 1

# 행
y = int(location[1])

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
# dx, dy 를 step = [(1, 2), (1, -2) ... ] 로 풀 수 도 있다.

count = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
print(count)
