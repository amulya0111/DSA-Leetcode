class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        def find(coins,amount,i,dp):
            
            if i==len(coins)-1:
                if amount%coins[i]==0:
                    return amount//coins[i]
                # else
                return float('inf')
            
            if coins[i]>amount:
                return find(coins,amount,i+1,dp)
            if dp[i][amount]!=-1:
                return dp[i][amount]
            pick=1+find(coins,amount-coins[i],i,dp)
            notpick=find(coins,amount,i+1,dp) 
            dp[i][amount]=min(pick,notpick)
            return min(pick,notpick)
        
        

        dp=[[-1]*(amount+1) for i in range(n)]
        ans = find(coins,amount,0,dp) 
        return ans if ans!=float('inf') else -1
        # for i in range(n-1,-1,-1):
        #     for target in range(1,amount+1):
        #         if target%coins[i]==0:
        #             dp[i][target]=target//coins[i]
        #         else:
            
