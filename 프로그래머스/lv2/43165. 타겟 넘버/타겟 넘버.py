def solution(numbers, target):
    sums = [0]
    for num in numbers:
        sub_tree = []
        for sum in sums:
            sub_tree.append(sum + num)
            sub_tree.append(sum - num)
        sums = sub_tree
    return sums.count(target)