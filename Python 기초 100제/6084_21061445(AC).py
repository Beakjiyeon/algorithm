a, b, c, d = map(int, input().split())
n = a*b*c*d
m = n/8/1024/1024
print('%.1f MB' %m)
