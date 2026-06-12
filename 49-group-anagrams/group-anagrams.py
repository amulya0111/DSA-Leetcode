class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in dic:
                dic[key] = []
            dic[key].append(word)
        return dic.values()