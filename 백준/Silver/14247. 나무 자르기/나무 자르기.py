n = int(input())
trees = list(map(int, input().split()))
grows = list(map(int, input().split()))
result = 0

# 성장률이 낮은 순으로 정렬
tree_grow_infos = sorted(zip(trees, grows), key=lambda x:x[1])

day = 0
for tree, grow in tree_grow_infos:
    # 본체 + 성장률 * 인덱스 => 성장률이 적은 나무 부터 벨 수 있다.
    result += tree + grow * day
    day += 1
print(result)
