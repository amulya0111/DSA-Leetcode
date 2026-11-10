mod=10**9+7
class Solution:
    def countSubsetsWithSumK(self, n, K, arr):
        # write your code here 
        dp=[0]*(K+1)
        dp[0]=1
        for i in range(n):
            for j in range(K,arr[i]-1,-1):
                dp[j]+= dp[j-arr[i]]
        return dp[K]%mod