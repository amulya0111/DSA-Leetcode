class Solution(object):
    def characterReplacement(self, s, k):
        freq={}
        r=0
        l=0
        ans=0
        if len(s)==1:
            return 1
        freq[s[r]]=freq.setdefault(s[r],0)+1
        maxfreq=1
        while l<=r and r<len(s)-1:
            
            if (r-l+1)-maxfreq<=k:
                r+=1
                freq[s[r]]=freq.setdefault(s[r],0)+1
                maxfreq=max(maxfreq,freq[s[r]])
            

            while r-l+1-maxfreq>k:
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans      



        


        