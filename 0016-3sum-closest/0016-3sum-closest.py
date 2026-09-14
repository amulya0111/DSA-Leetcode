class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        minadd=float('inf')
        maxsub=float('inf')
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            find= target-nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                curr=nums[l]+nums[r]
                if find<curr:
                    # curr to get lower
                    minadd=min(minadd,curr-find)
                    r-=1
                elif find>curr:
                    maxsub=min(maxsub,find-curr)
                    l+=1
                else:
                    return target
        if minadd<maxsub:
            return target+minadd
        else:
            return target-maxsub
