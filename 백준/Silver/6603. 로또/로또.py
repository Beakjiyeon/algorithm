if __name__ == '__main__':
    from itertools import combinations
    while True:
        array = list(map(int, input().split()))
        k = array[0]
        S = array[1:]
        if k == 0:
            break
        for combi in list(combinations(S, 6)):
            print(' '.join([str(d) for d in combi]))
        print()
