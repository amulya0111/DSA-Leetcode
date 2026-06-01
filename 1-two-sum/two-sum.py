class Solution(object):
    def twoSum(self,nums, target):
        mp = {}  # empty dictionary 

        for i in range(len(nums)):
            #we will use hashmap
            mp[nums[i]]=i
        for i in range(len(nums)):
            y=target-nums[i]
            # check if remining is in hashmap but not in same index 
            if y in mp and mp[y] != i:
                return [i,mp[y]]
        
        