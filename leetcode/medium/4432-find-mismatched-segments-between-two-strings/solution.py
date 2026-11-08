class Solution(object):
    def findMismatchedSegments(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[List[str]]
        """
        res=[]
        l=-1
        r=0
        while r<len(s1):
            if s1[r]==s2[r]:
                if r-l>1:
                    path1=s1[l+1:r]
                    path2=s2[l+1:r]
                    res.append([path1,path2])
                
                l=r
                r+=1
            else:
                if r==len(s1)-1 and r>l:
                    path1=s1[l+1:len(s1)]
                    path2=s2[l+1:len(s1)]
                    res.append([path1,path2])
                    
                r+=1
        return res
        
                