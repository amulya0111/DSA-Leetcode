class Solution(object):
    def minWindow(self, s, t):
    #     expand r → window becomes valid
    #           ↓
    #      shrink l
    #           ↓
    #   window becomes invalid
    #           ↓
    #      expand r again
        freq={}
        count={}
        ans=float('inf')
        for ch in t:
            freq[ch]=freq.setdefault(ch,0)+1
            count[ch]=0
        
        if len(s)<len(t):
            return ""
        l=0
        r=0
        ansl=0
        formed=0
        while r<len(s):
            if s[r] in count:
                count[s[r]]+=1
                if count[s[r]]==freq[s[r]]:
                    formed+=1
            while formed == len(freq):
                if r-l+1<ans:
                    ans=r-l+1
                    ansl=l
                if s[l] in count:
                    count[s[l]]-=1
                    if count[s[l]]<freq[s[l]]:
                        formed-=1
                l+=1
            r+=1
        if ans == float('inf'):
            return ""
        return s[ansl:ansl+ans]
            



            
