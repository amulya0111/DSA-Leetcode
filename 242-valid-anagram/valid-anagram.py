class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        count={}
        for sc in s:
            #dictionary.get(key, default_value)
            count[sc]=count.get(sc,0)+1
        for tc in t:
            count[tc]=count.get(tc,0)-1
            if count[tc]==-1:
                return False
        return True
        
            