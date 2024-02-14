n = int(input())

cnt = 0
while n > 0:
    # 11 케이스를 위해 제거
    # if n % 3 != 0 and n % 5 != 0:
    #     cnt = -1
    #     break

    if n % 5 == 0:
        m = n // 5
        n = n - m * 5
        cnt = cnt + m
    else:
        n = n - 3  # 18 케이스를 위해 %3 이 아닌 -3
        cnt = cnt + 1

if n != 0:
    cnt = -1
print(cnt)