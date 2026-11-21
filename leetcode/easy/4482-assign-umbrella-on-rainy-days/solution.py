class Solution(object):
    def assignUmbrella(self, rain):
        """
        :type rain: List[int]
        :rtype: List[str]
        """
        ans=[]
        n=len(rain)
        a="Alice"
        b="Bob"
        e="None"
        ac=0
        bc=0
        for i in range(n):
            if i==n-1 and rain[i]==1:
                ans.append(b)
                break
            if rain[i]==1:
                if rain[i+1]==1:
                    if ac<=bc:
                        ans.append(a)
                        ac+=1
                    else:
                        ans.append(b)
                        bc+=1
                else:
                    ans.append(b)
                    bc+=1
            else:
                ans.append(e)
        return ans