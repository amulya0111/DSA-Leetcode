
class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * col
        ans = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            for j in range(col + 1):
                curr = heights[j] if j < col else 0

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]

                    if stack:
                        w = j - stack[-1] - 1
                    else:
                        w = j

                    ans = max(ans, h * w)

                stack.append(j)

        return ans
