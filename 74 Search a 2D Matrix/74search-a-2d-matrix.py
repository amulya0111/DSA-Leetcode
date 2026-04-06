class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        for i in range(m):
            n=len(matrix[i])
            if target>=matrix[i][0] and target<=matrix[i][n-1]:
                for j in range(n):
                    if matrix[i][j]==target:
                        return True
                
                
        return False    
        