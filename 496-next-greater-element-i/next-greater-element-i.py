class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic={}
        n=len(nums2)
        t=1
        result=[]
        for num in nums2:
            for i in range(t,n):
                if nums2[i]>num:
                    dic[num]=nums2[i]
                    break
            t+=1
        for num in nums1:
            if num in dic:
                result.append(dic[num])
            else:
                result.append(-1)
        return result