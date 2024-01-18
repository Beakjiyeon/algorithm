'''
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

count = 0
for i in range(n):
    if count == k:
        break
    if a[i] < b[i]:
        a[i] = b[i]
        count += 1

print(sum(a))
'''

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        # b 원소값도 업데이트 필요함에 주의
        a[i], b[i] = b[i], a[i]
    # a의 원소가 b보다 크거나 같으면 탈출
    else:
        break

print(sum(a))
'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
