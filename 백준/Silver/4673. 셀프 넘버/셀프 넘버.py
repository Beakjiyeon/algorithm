numbers = []
for i in range(1, 10001):
    nums = list(map(int, list(str(i))))
    numbers.append(i + sum(nums))

for i in range(1, 10001):
    if i not in numbers:
        print(i)
