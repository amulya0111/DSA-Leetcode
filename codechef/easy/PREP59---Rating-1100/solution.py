t = int(input())
for _ in range(t):
    s = input().strip()
    stack = []
    is_valid = True
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                is_valid = False
                break
            stack.pop()
    
    if is_valid and len(stack) == 0:
        print(1)
    else:
        print(0)