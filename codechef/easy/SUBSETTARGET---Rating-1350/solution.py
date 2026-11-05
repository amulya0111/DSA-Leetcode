class Solution:
    def isSubsetSum(self, n, arr, target):
        # write your code here
        dp=[False]*n
        for i in range(n):
            pick=dp[ind]+dp[ind-1]
            notpick=dp[ind-1]
            dp=pick or notpick
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