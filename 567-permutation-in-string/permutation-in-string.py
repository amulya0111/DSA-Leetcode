class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        we have to use sliding window 
        use l,r for s2
        if the frequency of each alphabet matches its a true
        until r meets end :
            check particular subset , if alphabet is there 
        """
        l=0
        r=len(s1)-1
        count={}
        if len(s2)<len(s1):
            return False
        for ch in s1:
            count[ch]=count.get(ch,0)+1
        while r<len(s2):
            check={} 
            for i in range(l,r+1):
                if s2[i] in count:
                    check[s2[i]]=check.get(s2[i],0)+1
            if count == check:
                return True
            l=l+1
            r=r+1
        return False
                

        
        