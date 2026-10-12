# cook your dish here

t = int(input())

for _ in range(t):
    m, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    reach = x * y
    safe = 0

    for h in range(1, 101):
        watched = False

        for cop in a:
            if abs(h - cop) <= reach:
                watched = True
                break

        if not watched:
            safe += 1

    print(safe)
