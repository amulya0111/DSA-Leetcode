class Solution(object):
    def spiralOrder(self, matrix):
        rs=0
        re=len(matrix)-1
        cs=0
        ce=len(matrix[0])-1
        result=[]
        while rs<=re and cs <=ce:
            for i in range(cs,ce+1):
                result.append(matrix[rs][i])
            rs=rs+1
            for i in range(rs,re+1):
                result.append(matrix[i][ce])
            ce=ce-1
            if rs<=re:
                for i in range(ce,cs-1,-1):
                    result.append(matrix[re][i])
                re=re-1
            if cs<=ce:
                for i in range(re,rs-1,-1):
                    result.append(matrix[i][cs])
                cs=cs+1
        return result        