n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
print(arr)

'''
sort() vs sorted()
list.sort() : 원본 값 수정
sorted(list) : 원본 값은 그대로고 정렬 값을 반환한다.
'''
