def palindromeinrange():
    n = int(input())
    m = int(input())
    while n <= m:
        c = str(n)
        if c == c[::-1]:
            print(n, end=' ')
        n += 1
    return 0

palindromeinrange()
