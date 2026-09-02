class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=max(nums)
        right=sum(nums)
        sub=[]
        ans=[]

        while left<right:
            
            summ=0
            count=1
            for num in nums:
                limit=(left+right)//2
                if not sub or (summ+num)<=limit:
                    sub.append(num)
                    summ=summ+num
                else:
                    count+=1
                    ans.append(sub)
                    sub=[num]
                    summ=num
            if count <= k:
                right=limit
            else:
                left=limit+1

            
        ans.append(sub)
        return left
        
