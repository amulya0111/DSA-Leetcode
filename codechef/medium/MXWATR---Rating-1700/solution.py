# cook your dish here
t = int(input())

def max_vol(H):
    if len(H) < 3:
        return 0
    max_height = 0
    cur_vol = 0
    max_v = 0
    for h in H:
        if h >= max_height:
            max_height = h 
            max_v = max(max_v, cur_vol)
            cur_vol = 0 
        else:
            cur_vol += max_height - h
    return max_v

for _ in range(t):
    n = int(input())
    height = list(map(int, input().split()))
    
    # Find the tallest wall in the pool
    h_max = max(height)
    h_max_ind = height.index(h_max)
    
    # Split the pool into left part and right part relative to the tallest wall
    H_left = height[:h_max_ind + 1]
    H_right = height[h_max_ind:]
    H_right.reverse()
    
    max_left = max_vol(H_left)
    max_right = max_vol(H_right)
    
    print(max(max_left, max_right))