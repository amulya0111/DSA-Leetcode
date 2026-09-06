# from math import gcd
class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        maxi = 0
        for fixed in points:
            slope={}
            for point in points:
                if fixed==point:
                    continue
                x1=fixed[0]
                x2=point[0]
                y1=fixed[1]
                y2=point[1]
                dx=x2-x1
                dy=y2-y1
                if dx < 0:
                    dy = -dy
                    dx = -dx
                if dx == 0:
                    curr = "vertical"
                else:
                    g = gcd(abs(dy), abs(dx))
                    dy = dy // g
                    dx = dx // g
                    curr = (dy, dx)
                slope[curr] = slope.setdefault(curr, 0) + 1
            maxi = max(maxi, max(slope.values()) + 1)
        return maxi