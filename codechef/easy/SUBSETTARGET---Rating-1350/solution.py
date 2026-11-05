class Solution:
    def isSubsetSum(self, n, arr, target):
        # write your code here
        dp=[False]*(target+1)
        dp[0]=True
        for i in range(n):
            for j in range(target,arr[i]-1,-1):
                if dp[s-val]:
                    dp[s]=True
        # def find(ind,arr,target):
        #     if ind==0:
        #         if arr[ind]==target:
        #             return True
        #         else:
        #             return False
        #     if arr[ind]>target:
        #         return False
        #     pick = arr[ind]+find(ind-1,arr,target-arr[ind])
        #     notpick=find(ind-1,arr,target)
        #     return pick or notpick
        # return find(n-1,arr,target)