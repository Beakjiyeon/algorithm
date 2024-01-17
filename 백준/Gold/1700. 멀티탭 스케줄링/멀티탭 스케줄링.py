from collections import Counter

def trim_already_in_multitap(to_adds, multitap):
    tmp = []
    for to_add in to_adds:
        if to_add in multitap and to_add not in tmp: # 가장 마지막인 순으로 해야함 todo
            tmp.append(to_add)
    return tmp

def remove_use(index):
    #print(mulitap)
    # 앞으로 꽂아야 하는 전자 기기들
    to_adds = uses[index:]

    # 지금 멀티탭에 꽂혀있는 전자기기들 중에 앞으로 사용이 안 될 전자기기가 있는지
    for multi in mulitap:
        if multi not in to_adds:
            mulitap.remove(multi)
            return 0

    # 멀티탭에 꽂혀있는 전자기기들 중에 가장 마지막에 사용될
    to_remove = trim_already_in_multitap(uses[index:], mulitap)
    # print('tr', to_remove)
    if to_remove:
        mulitap.remove(to_remove[-1])
        return 0


if __name__ == '__main__':
    count = 0
    mulitap = []
    n, k = map(int, input().split())
    uses = [int(x) for x in input().split()]
    counts = Counter(uses)
    sorted_keys = sorted(counts, key=counts.get)

    for i in range(len(uses)):
        # 이미 꽂혀 있음
        if uses[i] in mulitap:
            continue
        # 멀티 탭 꽉 참
        if len(mulitap) == n:
            remove_use(i)
            count += 1
        mulitap.append(uses[i])
    print(count)

'''
2 7
2 3 2 3 1 2 7
: 2

**
2 13
2 3 1 3 1 3 1 3 2 2 2 2 2
: 2

2 15
3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
: 2

3 8
1 2 3 4 1 1 1 2
: 1

1 3
1 2 1
: 2

3 6
1 2 3 4 1 2
: 1

6 7
1 1 1 1 1 1 2
: 0

***
2 10
1 2 3 2 3 2 2 2 1 2 # 여기서 (1, 2) 에 3을 꽂을 때, 이미 꽂혀있는 1, 2에 대해 1은 7번째에 2는 2번째에 사용된다. 1이 더 나중에 쓰이므로 1을 뺀다.
: 2

5 20
1 2 3 4 1 1 1 3 3 2 5 7 20 1 3 4 2 1 9 19
: 4

**
3 20
1 2 3 4 4 3 5 8 9 19 20 1 2 3 20 4 1 2 3 4
: 10

**
3 10
2 3 1 4 2 3 2 4 1 4
: 2

'''