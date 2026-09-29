class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        firstcol = False
        # use first m and first column as flags
        for i in range(m):
            if matrix[i][0] == 0:
                firstcol = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # use the flags to set zeroes
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # first m
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        # first column
        if firstcol:
            for i in range(m):
                matrix[i][0] = 0