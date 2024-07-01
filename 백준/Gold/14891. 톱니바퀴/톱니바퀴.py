w1 = list(map(int, list(input())))
w2 = list(map(int, list(input())))
w3 = list(map(int, list(input())))
w4 = list(map(int, list(input())))
w = [w1, w2, w3, w4]
terms = int(input())

def move_right(w_num, direction):
    last_one = [w[w_num][-1]]
    front = w[w_num][0:-1]
    w[w_num] = last_one + front


def move_left(w_num, direction):
    first_one = [w[w_num][0]]
    back = w[w_num][1:]
    w[w_num] = back + first_one


def move_wheel(w_num, direction):
    # 방향 1 >> 시계 방향
    if direction == 1:
        move_right(w_num, direction)
    # 방향 -1 >> 반시계 방향
    else:
        move_left(w_num, direction)

def has_effect_right(changed, to_change):
    return w[changed][2] != w[to_change][6]


# def move_recursive_right(target, direction):
#     # target 바퀴, target + 1 바퀴 비교
#     while target <= 2:
#         ef = has_effect_right(target, target + 1)
#         # 다른 극 > 해당 바퀴 회전 > 반대 방향
#         if ef:
#             print("오른쪽 바뀝니다.")
#             direction *= -1
#             target += 1
#             move_wheel(target, direction)
#         else:
#             break
#     pass


def has_effect_left(changed, to_change):
    return w[changed][6] != w[to_change][2]


# def move_recursive_left(target, direction):
#     # target 바퀴, target + 1 바퀴 비교
#     while target >= 1:
#         ef = has_effect_left(target, target - 1)
#         # 다른 극 > 해당 바퀴 회전 > 반대 방향
#         if ef:
#             print("왼쪽 바뀝니다.")
#             direction *= -1
#             target -= 1
#             move_wheel(target, direction)
#         else:
#             break
#     pass


def move_recursive_right2(target, direction):
    # target 바퀴, target + 1 바퀴 비교
    to_rotates = []
    while target <= 2:
        ef = has_effect_right(target, target + 1)
        # 다른 극 > 해당 바퀴 회전 > 반대 방향
        if ef:
            direction *= -1
            target += 1
            to_rotates.append((target, direction))
        else:
            break
    for to_rotate in to_rotates:
        move_wheel(to_rotate[0], to_rotate[1])


def move_recursive_left2(target, direction):
    # target 바퀴, target + 1 바퀴 비교
    to_rotates = []
    while target >= 1:
        ef = has_effect_left(target, target - 1)
        # 다른 극 > 해당 바퀴 회전 > 반대 방향
        if ef:
            direction *= -1
            target -= 1
            to_rotates.append((target, direction))
        else:
            break
    for to_rotate in to_rotates:
        move_wheel(to_rotate[0], to_rotate[1])

for term in range(0, terms):

    w_num, direction = map(int, input().split(' '))
    # 연쇄 회전 - 오른쪽

    r_idx = w_num - 1
    # move_recursive_right(r_idx, direction)
    move_recursive_right2(r_idx, direction)

    # 연쇄 회전 - 왼쪽
    l_idx = w_num - 1
    move_recursive_left2(l_idx, direction)

    # 요청 바퀴 회전
    move_wheel(w_num - 1, direction)
# 점수 계산
score = 0
if w[0][0] == 0:
    score += 0
else:
    score += 1

if w[1][0] == 0:
    score += 0
else:
    score += 2

if w[2][0] == 0:
    score += 0
else:
    score += 4

if w[3][0] == 0:
    score += 0
else:
    score += 8

print(score)