class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        r=0
        count=k
        ones=0
        ans=0
        while r<len(nums):
            if nums[r]==1:
                ones+=1
                r+=1
            else:
                if count>0:
                    ones+=1
                    count-=1
                    r+=1
                else:
                    ans=max(ans,ones)
                    while count==0:
                        if nums[l]==0:
                            count+=1
                        ones-=1
                        l+=1
                    ones+=1
                    count-=1
                    r+=1
            
                            
        return max(ans,ones)

            


            
