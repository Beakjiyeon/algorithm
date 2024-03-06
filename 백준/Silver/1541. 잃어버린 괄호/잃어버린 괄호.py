def get_sum(cmd):
    return sum(list(map(int, cmd.split('+'))))


full = input()
groups = full.split('-')

result = get_sum(groups[0])
for group in groups[1:]:
    plus_value = get_sum(group)
    result -= plus_value
print(result)
