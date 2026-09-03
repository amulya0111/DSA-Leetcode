class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1]*len(ratings)
        n=len(ratings)
        if n==1:
            return 1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                if candies[i]<=candies[i-1]:
                    diff=candies[i-1]-candies[i]
                    candies[i]+=diff+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                if candies[i]<=candies[i+1]:
                    diff=candies[i+1]-candies[i]
                    candies[i]+=diff+1
        return sum(candies)

