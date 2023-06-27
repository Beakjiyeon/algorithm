def get_next():
    #print("호출됨")
    if len(result) == m:
        print(*result)
        #result.pop()
        return

    for option in options:
        #if option not in result:
        result.append(option)
        get_next()
        result.pop()



if __name__ == '__main__':
    n, m = map(int, input().split())
    options = [i + 1 for i in range(n)]
    for i, option in enumerate(options):
        #print("### ", i)
        result = [option]
        get_next()