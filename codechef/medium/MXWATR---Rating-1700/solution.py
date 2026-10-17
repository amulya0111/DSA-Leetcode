# cook your dish here
t = int(input())

def max_vol(arr):
    if len(arr) < 3:
        return 0
    max_height = 0
    cur_vol = 0
    max_v = 0
    for h in arr:
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
    
    h_max = max(height)
    h_max_ind = height.index(h_max)
    
    h_left = height[:h_max_ind + 1]
    h_right = height[h_max_ind:]
    h_right.reverse()
    
    max_left = max_vol(h_left)
    max_right = max_vol(h_right)
    
    print(max(max_left, max_right))