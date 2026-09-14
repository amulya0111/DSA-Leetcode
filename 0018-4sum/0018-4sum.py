class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        op=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                find=target-nums[i]-nums[j]
                l=j+1
                r=len(nums)-1

                while l<r:
                    
                    curr=nums[l]+nums[r]

                    if curr<find:
                        l+=1
                    elif curr>find:
                        r-=1
                    else:
                        op.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
        return op        
        