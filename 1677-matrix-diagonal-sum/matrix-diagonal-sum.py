class Solution(object):
    def diagonalSum(self, mat):
        """
        00 01 02 03    00 01 02
        10 11 12 13    10 11 12
        20 21 22 23    20 21 22
        30 31 32 33

        i=j for primary
        (i range(len()-1,-1,-1):mat[][])
        """
        sum=0
        count=len(mat)-1
        for i in range(len(mat)): #0,1,2,3
            sum+=mat[i][i]
            if i!=count:
                sum+=mat[i][count]
            count-=1
        return sum