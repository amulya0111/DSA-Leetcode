class Solution(object):
    def lastVisitedCell(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: List[int]
        """
        m=len(grid)
        n=len(grid[0])
        s=set()
        i=0
        j=0
        lastvisited=(0,0)
        s.add(lastvisited)
        while True:
            if grid[i][j]=="R":
                j+=1
            elif grid[i][j]=="D":
                i+=1
            elif grid[i][j]=="L":
                j-=1
            elif grid[i][j]=="U":
                i-=1            
            if not i>=0 or not j>=0 or not i<m or not j<n or (i,j) in s:
                return list(lastvisited)
            # s.append(lastvisited)
            lastvisited=(i,j)
            s.add(lastvisited)
        return lastvisited