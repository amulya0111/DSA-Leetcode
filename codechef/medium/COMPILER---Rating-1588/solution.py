# cook your dish here
t=int(input())
for _ in range(t):
    stack=[]
    s=input()
    count=0
    for ch in s:
        if ch=="<":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
                count+=2
    print(count)