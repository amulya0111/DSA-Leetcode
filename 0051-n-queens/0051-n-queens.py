class Solution(object):
    def solveNQueens(self, n):
        ans=[]
        board = [['.'] * n for i in range(n)]
        ldia=[0]*(2*n-1)
        udia=[0]*(2*n-1)
        lrow=[0]*n
        def solve(col,ans,udia,ldia,lrow,n):
            for row in range(n):
                if col==n:
                    temp = []
                    for i in range(n):
                        temp.append(''.join(board[i]))
                    ans.append(temp)
                    return
                if lrow[row]==1 or udia[n-1-row+col]==1 or ldia[row+col]==1:
                    continue
                else:
                    
                    lrow[row]=1
                    ldia[row+col]=1
                    udia[n-1+col-row]=1
                    board[row][col]='Q'

                    solve(col+1,ans,udia,ldia,lrow,n)
                    
                    lrow[row]=0
                    ldia[row+col]=0
                    udia[n-1+col-row]=0
                    board[row][col]='.'
            return ans
        solve(0,ans,udia,ldia,lrow,n)
        return ans
                 