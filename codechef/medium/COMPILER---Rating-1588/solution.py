# cook your dish here
t=int(input())
for _ in range(t):
    stack=[]
    s=input()
    ans=0
    for i in range(len(s)):
        if s[i]=="<":
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                break
        if not stack:
            ans=i+1
    print(ans)