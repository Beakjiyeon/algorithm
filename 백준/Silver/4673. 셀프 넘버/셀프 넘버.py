

numbers =[]
for i in range(1, 10001):
    nums = list(map(int, list(str(i))))
    number = i + sum(nums)
    numbers.append(number)

for i in range(1, 10001):
    if i not in numbers:
        print(i)