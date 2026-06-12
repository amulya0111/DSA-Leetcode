class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        l=0
        n=len(p)
        count={}
        win={}
        result=[]
        for ch in p:
            count[ch]=count.get(ch,0)+1
        for i in range(len(p)):
            win[s[i]]=win.get(s[i],0)+1
        if count==win:
            result.append(0)

        for r in range(n,len(s)):
            win[s[l]]=win.get(s[l],0)-1
            if win[s[l]] == 0:
                del win[s[l]]
            l+=1
            win[s[r]]=win.get(s[r],0)+1
            if count==win:
                result.append(l)
        return result
        