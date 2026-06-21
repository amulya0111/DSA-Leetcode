
class Solution(object):
    def largestRectangleArea(self, heights):

        stack=[]
        area=0
        n=len(heights)

        for i in range(n):

            while stack and heights[i]<heights[stack[-1]]:
                y=stack.pop()
                h=heights[y]
                if len(stack)==0:
                    w=i
                else:
                    w=i-stack[-1]-1
                area=max(area,h*w)

            stack.append(i)
        while stack:

            y=stack.pop()
            h=heights[y]

            if len(stack)==0:
                w=n
            else:
                w=n-stack[-1]-1
            area=max(area,h*w)

        return area