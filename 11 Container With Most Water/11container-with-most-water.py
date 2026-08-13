class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1        
        max_l=0
        max_r=0
        area=0
        while r>=l:
            width = r-l
            max_height=min(height[l],height[r])
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
            area=max(max_height*width,area)
        return area
