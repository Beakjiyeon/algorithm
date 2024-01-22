n = int(input())

infos = []
for _ in range(n):
    name, kr, eng, math = input().split()
    infos.append((name, int(kr), int(eng), int(math)))

infos.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for info in infos:
    print(info[0])
