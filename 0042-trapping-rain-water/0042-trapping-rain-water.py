class Solution(object):
    def trap(self, height):
        stack = []
        water = 0
        n = len(height)

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                y = stack.pop()

                if not stack:
                    break

                h = min(height[i], height[stack[-1]]) - height[y]
                w = i - stack[-1] - 1

                water += h * w

            stack.append(i)

        return water
