n, l = map(int, input().split())
spots = list(map(int, input().split()))

spots = sorted(spots)

count = 0
t_start = 0
t_end = 0

for spot in spots:
    # 테이프 끝 범위가 누수 지점을 가리지 못한 경우 (t_end=0 인 경우는 첫 번째라 제외) 
    if t_end != 0 and t_end > spot:
        continue
    # 누수 지점을 가리기 위한 시작, 끝 범위
    start = spot - 0.5
    end = spot + 0.5

    # 테이프 시작, 끝 범위
    t_start = start
    t_end = t_start + l

    # 테이프 수
    count += 1

print(count)
