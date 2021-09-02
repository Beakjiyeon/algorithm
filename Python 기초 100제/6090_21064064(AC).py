s, a, b, n = map(int, input().split())
list = []
list.append(s)

for i in range(n-1):
    list.append(list[i]*a + b)
    # list[i] = list[0] // 아직 list[1]은 None인데 이걸 인덱싱 불가한 듯
print(list[n-1])


'''
def calculate(number):
    if list[n-1] == None:
        calculate(n-1)
    k = list[n-1] * a + b
    list.append(k)
    return k

calculate(n)
'''
