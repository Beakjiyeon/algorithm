i = 1
while True:
    case = input()

    if case == '0 0 0':
        break

    l, p, v = map(int, case.split())

    result = (v // p) * l # 몫
    remainder = v % p  # 나머지

    if remainder <= l:
        result += remainder
    else:
        result += l

    print(f"Case {i}: {result}")
    i += 1