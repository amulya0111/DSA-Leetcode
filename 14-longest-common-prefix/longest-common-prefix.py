class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        while true
        use i to iterate
        check from word to word of letter is same 
        stor the prfix length
        if the length reduced in nex itr , choose smaller length
        """
        if len(strs)==1:
            return strs[0]
        j=min(len(strs[0]),len(strs[1]))
        for i in range(len(strs)-1):
            curr=0
            for k in range(min(len(strs[i]),len(strs[i+1]))):
                if len(strs[i+1])<j:
                    j=len(strs[i+1])
                if strs[i][k]==strs[i+1][k]:
                    curr+=1
                else:
                    break
            j=min(curr,j)
        return strs[0][0:j]
