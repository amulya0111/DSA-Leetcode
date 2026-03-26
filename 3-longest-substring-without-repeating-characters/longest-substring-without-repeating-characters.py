class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #we will use sliding window technique in this 
        #use two pointers l and r
        l=0
        r=0
        #one set to check duplicates 
        sett=set()
        #one count 
        longest=0
        #create a condition , lets try r loop
        for r in range(len(s)):
            #check if the item on r is present in set (if present , its a dupe)
            while s[r] in sett:
                #remove the element at s[l] from set and keep incrementing s[l]
                sett.remove(s[l])
                l+=1  
            #the new string we have now is made of unique elemts , store its length in w
            w=r-l+1
            #compare with the previous longest string encountered
            longest=max(longest,w)
            sett.add(s[r])
        return longest
            

            

        