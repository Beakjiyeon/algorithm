a, b, c = map(int, input().split())
n = a*b*c
m = n/8/1024/1024
print('%.2f MB' %m)
