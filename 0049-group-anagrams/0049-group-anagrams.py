class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        for word in strs:
            key = "".join(sorted(word))
            dic.setdefault(key,[]).append(word)
            
        return dic.values()