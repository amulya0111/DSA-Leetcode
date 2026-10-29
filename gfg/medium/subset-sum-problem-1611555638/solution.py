class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n=len(arr)
        k=sum
        dp=[[False]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        # defining l=the last element we captured during memoization , if the value is < main target just add
        if arr[0]<=k:
            dp[0][arr[0]]=True
        for i in range(1,n):
            for target in range(1,k+1):
                # first not take 
                not_take=dp[i-1][target]
                take=False
                if arr[i]<=target:
                    take=dp[i-1][target-arr[i]]
                dp[i][target]=take or not_take
        return dp[n-1][k]