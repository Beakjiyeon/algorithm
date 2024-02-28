def hanoi(n, from_pos, to_pos, aux_pos):
    way = str(from_pos) + " " + str(to_pos)
    if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        print(way)
        return 1
    # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
    count1 = hanoi(n - 1, from_pos, aux_pos, to_pos)

    # 가장 큰 원반을 목적지로 이동 1
    print(way)
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    count2 = hanoi(n - 1, aux_pos, to_pos, from_pos)
    return count1 + 1 + count2


n = int(input())
print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3, 2)
