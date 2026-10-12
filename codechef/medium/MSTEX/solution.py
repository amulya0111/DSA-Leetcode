# cook your dish here

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    c.sort(reverse=True)
    print(sum(c[:k]))
