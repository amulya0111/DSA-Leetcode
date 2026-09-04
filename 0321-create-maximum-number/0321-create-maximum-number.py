class Solution(object):
    def merge(self,find1,find2):
        i=0
        j=0
        result=[]
        while i<len(find1) and j<len(find2):
            if find1[i]<find2[j]:
                result.append(find2[j])
                j+=1
            elif find2[j]<find1[i]:
                result.append(find1[i])
                i+=1
            else:
                # instead of
                # if i==len(find1)-1 or (j<len(find2)-1 and find1[i:] > find2[j:]):
                # use this
                if find1[i:] > find2[j:]:
                    result.append(find1[i])
                    i+=1
                else:
                    result.append(find2[j])
                    j+=1
        result.extend(find1[i:])
        result.extend(find2[j:])
        return result 
    def compare(self,result,ans):
        if not ans:
            ans=result
        else:
            ans=max(ans,result)
        return ans

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        for x in range(max(0, k-len(nums2)), min(k, len(nums1))+1):
            y=k-x
            removals =len(nums1)-x
            find1=[]
            for num in nums1:
                while removals > 0 and find1 and find1[-1] < num:
                    find1.pop()
                    removals -= 1
                find1.append(num)
            find1 = find1[:x]
            find2=[]
            removals=len(nums2)-y
            for num in nums2:
                while removals > 0 and find2 and find2[-1] < num:
                    find2.pop()
                    removals -= 1
                find2.append(num)
            find2 = find2[:y]
            result=self.merge(find1,find2)
            ans=self.compare(result,ans)
            
        return ans
                    

        