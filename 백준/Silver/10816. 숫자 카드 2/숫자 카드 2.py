n = int(input())
given = list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

from collections import Counter

given_count = Counter(given)

for t in test:
    print(given_count[t], end=' ')