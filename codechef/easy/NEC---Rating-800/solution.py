# cook your dish here

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    k %= n
    ans = arr[k:] + arr[:k]

    print(*ans)
